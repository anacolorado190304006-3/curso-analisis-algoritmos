
"""Experimentos de rendimiento para lista enlazada y tabla hash.

Se comparan los tiempos de búsqueda de guías inexistentes y se estudia
el efecto del factor de carga en una tabla hash con encadenamiento.
"""

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


SEMILLA = 42
CANTIDAD_CONSULTAS_A = 1_000
CANTIDAD_CONSULTAS_B = 200_000
REPETICIONES = 7

DIRECTORIO_GRAFICAS = Path(__file__).parent / "graficas"


def generar_guias(cantidad: int, semilla: int = SEMILLA) -> list[int]:
    """Genera guías únicas de diez dígitos.

    Args:
        cantidad: Número de guías que se deben generar.
        semilla: Semilla para reproducir los resultados.

    Returns:
        Lista de guías enteras únicas.
    """
    generador = random.Random(semilla)
    return generador.sample(
        range(1_000_000_000, 10_000_000_000),
        cantidad,
    )


def generar_guias_inexistentes(
    existentes: set[int],
    cantidad: int,
    semilla: int = 7,
) -> list[int]:
    """Genera guías que no pertenecen al conjunto de existentes.

    Args:
        existentes: Conjunto de guías almacenadas.
        cantidad: Cantidad de consultas ausentes que se generarán.
        semilla: Semilla para reproducir las consultas.

    Returns:
        Lista de guías inexistentes.
    """
    generador = random.Random(semilla)
    consultas: list[int] = []

    while len(consultas) < cantidad:
        guia = generador.randint(1_000_000_000, 9_999_999_999)

        if guia not in existentes:
            consultas.append(guia)

    return consultas


def construir_lista(guias: list[int]) -> ListaEnlazada:
    """Construye una lista enlazada con las guías recibidas.

    Args:
        guias: Guías que se almacenarán.

    Returns:
        Lista enlazada construida.
    """
    lista = ListaEnlazada()

    for guia in guias:
        lista.insertar(guia, "En camino")

    return lista


def construir_tabla(guias: list[int], m: int) -> TablaHash:
    """Construye una tabla hash con las guías recibidas.

    Args:
        guias: Guías que se almacenarán.
        m: Número de casillas de la tabla.

    Returns:
        Tabla hash construida.
    """
    tabla = TablaHash(m)

    for guia in guias:
        tabla.insertar(guia, "En camino")

    return tabla



def medir_busquedas(
    estructura: ListaEnlazada | TablaHash,
    consultas: list[int],
    repeticiones: int = REPETICIONES,
) -> float:
    """Mide la mediana del tiempo por búsqueda fallida.

    Args:
        estructura: Estructura que se evaluará.
        consultas: Guías inexistentes que se buscarán.
        repeticiones: Cantidad de repeticiones del experimento.

    Returns:
        Mediana del tiempo por búsqueda, en segundos.
    """
    if not consultas:
        raise ValueError("La lista de consultas no puede estar vacía.")

    # Calentamiento previo, excluido de la medición.
    for guia in consultas[:min(1000, len(consultas))]:
        estructura.buscar(guia)

    tiempos: list[float] = []

    for _ in range(repeticiones):
        inicio = time.perf_counter()

        for guia in consultas:
            estructura.buscar(guia)

        fin = time.perf_counter()

        tiempo_por_busqueda = (fin - inicio) / len(consultas)
        tiempos.append(tiempo_por_busqueda)

    return statistics.median(tiempos)


def verificar_equivalencia(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
) -> None:
    """Comprueba que ambas estructuras devuelvan los mismos estados.

    Args:
        lista: Lista enlazada que se comparará.
        tabla: Tabla hash que se comparará.
        guias: Guías existentes que se utilizarán como muestra.
    """
    muestra = guias[:min(100, len(guias))]

    for guia in muestra:
        assert lista.buscar(guia) == tabla.buscar(guia)


def experimento_a() -> list[tuple[int, float, float, float]]:
    """Compara lista y tabla al aumentar la cantidad de guías.

    Returns:
        Resultados con n, factor de carga y tiempos de ambas estructuras.
    """
    cantidades = [100, 500, 1_000, 5_000, 20_000, 50_000]

    tamanos = {
        100: 53,
        500: 251,
        1_000: 503,
        5_000: 2_503,
        20_000: 10_007,
        50_000: 25_013,
    }

    resultados: list[tuple[int, float, float, float]] = []

    print("\nEXPERIMENTO A: LISTA ENLAZADA VS TABLA HASH")
    print("-" * 82)
    print(
        f"{'n':>10} {'Alfa':>10} {'Lista (s)':>20} "
        f"{'Tabla (s)':>20}"
    )

    for cantidad in cantidades:
        guias = generar_guias(cantidad)
        existentes = set(guias)

        consultas = generar_guias_inexistentes(
            existentes,
            CANTIDAD_CONSULTAS_A,
            semilla=7,
        )

        lista = construir_lista(guias)
        tabla = construir_tabla(guias, tamanos[cantidad])

        verificar_equivalencia(lista, tabla, guias)

        tiempo_lista = medir_busquedas(lista, consultas)
        tiempo_tabla = medir_busquedas(tabla, consultas)
        alfa = tabla.factor_carga()

        resultados.append(
            (cantidad, alfa, tiempo_lista, tiempo_tabla)
        )

        print(
            f"{cantidad:>10} {alfa:>10.4f} "
            f"{tiempo_lista:>20.10f} {tiempo_tabla:>20.10f}"
        )

    graficar_experimento_a(resultados)

    return resultados


def graficar_experimento_a(
    resultados: list[tuple[int, float, float, float]],
) -> None:
    """Genera la gráfica comparativa de tiempos de búsqueda.

    Args:
        resultados: Resultados del experimento A.
    """
    cantidades = [fila[0] for fila in resultados]
    tiempos_lista = [fila[2] for fila in resultados]
    tiempos_tabla = [fila[3] for fila in resultados]

    plt.figure(figsize=(10, 6))

    plt.plot(
        cantidades,
        tiempos_lista,
        marker="o",
        label="Lista enlazada",
    )

    plt.plot(
        cantidades,
        tiempos_tabla,
        marker="s",
        label="Tabla hash",
    )

    plt.title("Tiempo de búsqueda: lista enlazada vs tabla hash")
    plt.xlabel("Cantidad de guías (n)")
    plt.ylabel("Tiempo promedio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        DIRECTORIO_GRAFICAS / "lista_vs_tabla.png",
        dpi=300,
    )

    plt.close()


def experimento_b() -> list[tuple[float, float, int]]:
    """Estudia el tiempo de búsqueda para distintos factores de carga.

    Mantiene 20.000 guías y cambia el tamaño de la tabla hash.
    Utiliza 20.000 consultas fallidas por repetición.

    Returns:
        Resultados con factor de carga, tiempo promedio y tamaño de tabla.
    """
    cantidad = 20_000

    tamanos = [
        40_009,
        20_011,
        5_003,
        2_003,
    ]

    guias = generar_guias(cantidad)
    existentes = set(guias)

    consultas = generar_guias_inexistentes(
        existentes,
        CANTIDAD_CONSULTAS_B,
        semilla=17,
    )

    lista = construir_lista(guias)

    resultados: list[tuple[float, float, int]] = []

    print("\nEXPERIMENTO B: TIEMPO SEGÚN FACTOR DE CARGA")
    print("-" * 82)
    print(
        f"{'Alfa':>10} {'m':>10} "
        f"{'Tiempo tabla (s)':>22} {'Consultas':>15}"
    )

    for m in tamanos:
        tabla = construir_tabla(guias, m)

        verificar_equivalencia(lista, tabla, guias)

        tiempo_tabla = medir_busquedas(tabla, consultas)
        alfa = tabla.factor_carga()

        resultados.append((alfa, tiempo_tabla, m))

        print(
            f"{alfa:>10.4f} {m:>10} "
            f"{tiempo_tabla:>22.10f} "
            f"{len(consultas):>15}"
        )

    graficar_experimento_b(resultados)

    return resultados


def graficar_experimento_b(
    resultados: list[tuple[float, float, int]],
) -> None:
    """Genera la gráfica del tiempo de búsqueda según el factor de carga.

    Args:
        resultados: Resultados del experimento B.
    """
    factores = [fila[0] for fila in resultados]
    tiempos = [fila[1] for fila in resultados]

    plt.figure(figsize=(10, 6))

    plt.plot(
        factores,
        tiempos,
        marker="o",
        label="Tabla hash",
    )

    plt.title("Tiempo de búsqueda según el factor de carga")
    plt.xlabel("Factor de carga (α)")
    plt.ylabel("Tiempo promedio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        DIRECTORIO_GRAFICAS / "tiempo_vs_alfa.png",
        dpi=300,
    )

    plt.close()


def main() -> None:
    """Ejecuta los experimentos y genera las gráficas."""
    DIRECTORIO_GRAFICAS.mkdir(parents=True, exist_ok=True)

    resultados_a = experimento_a()
    resultados_b = experimento_b()

    assert len(resultados_a) == 6
    assert len(resultados_b) == 4

    print("\nEXPERIMENTOS FINALIZADOS")
    print("Gráficas generadas correctamente:")
    print(" - graficas/lista_vs_tabla.png")
    print(" - graficas/tiempo_vs_alfa.png")


if __name__ == "__main__":
    main()
