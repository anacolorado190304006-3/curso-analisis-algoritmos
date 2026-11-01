
"""Pruebas automatizadas para las estructuras del laboratorio 3."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_lista_vacia() -> None:
    """Comprueba el comportamiento de una lista vacía."""
    lista = ListaEnlazada()

    assert lista.buscar(1234567890) is None
    assert lista.tamano == 0


def probar_insercion_y_busqueda_lista() -> None:
    """Comprueba inserciones y búsquedas en la lista enlazada."""
    lista = ListaEnlazada()

    lista.insertar(1234567890, "En camino")
    lista.insertar(9876543210, "Entregado")
    lista.insertar(1111111111, "En bodega")

    assert lista.tamano == 3
    assert lista.buscar(1234567890) == "En camino"
    assert lista.buscar(9876543210) == "Entregado"
    assert lista.buscar(1111111111) == "En bodega"
    assert lista.buscar(2222222222) is None


def probar_tabla_vacia() -> None:
    """Comprueba el comportamiento de una tabla hash vacía."""
    tabla = TablaHash(7)

    assert tabla.buscar(1234567890) is None
    assert tabla.tamano == 0
    assert tabla.factor_carga() == 0.0


def probar_colisiones() -> None:
    """Comprueba que varias guías en la misma casilla se recuperen."""
    tabla = TablaHash(7)

    # Las tres guías producen el índice 3 al dividir entre 7.
    tabla.insertar(10, "En camino")
    tabla.insertar(24, "Entregado")
    tabla.insertar(17, "En bodega")

    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3

    assert tabla.buscar(10) == "En camino"
    assert tabla.buscar(24) == "Entregado"
    assert tabla.buscar(17) == "En bodega"

    assert tabla.casillas[3].tamano == 3
    assert tabla.tamano == 3
    assert abs(tabla.factor_carga() - (3 / 7)) < 1e-12


def probar_tabla_y_lista_equivalentes() -> None:
    """Compara los resultados de ambas estructuras en 20 conjuntos.

    Cada conjunto contiene guías aleatorias y consultas existentes
    y ausentes. Se utiliza una semilla fija para reproducibilidad.
    """
    generador = random.Random(42)

    for _ in range(20):
        cantidad = generador.randint(20, 100)
        guias = generador.sample(range(1_000_000_000, 9_999_999_999), cantidad)

        lista = ListaEnlazada()
        tabla = TablaHash(101)

        estados: dict[int, str] = {}

        for guia in guias:
            estado = generador.choice(
                ["En preparación", "En camino", "Entregado", "En bodega"]
            )

            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)
            estados[guia] = estado

        # Consultas existentes.
        for guia in guias:
            assert lista.buscar(guia) == estados[guia]
            assert tabla.buscar(guia) == estados[guia]

        # Consultas ausentes.
        for _ in range(20):
            guia_ausente = generador.randint(1_000_000_000, 9_999_999_999)

            while guia_ausente in estados:
                guia_ausente = generador.randint(
                    1_000_000_000, 9_999_999_999
                )

            assert lista.buscar(guia_ausente) is None
            assert tabla.buscar(guia_ausente) is None


def ejecutar_pruebas() -> None:
    """Ejecuta todas las pruebas automatizadas."""
    probar_lista_vacia()
    probar_insercion_y_busqueda_lista()
    probar_tabla_vacia()
    probar_colisiones()
    probar_tabla_y_lista_equivalentes()

    print("Todas las pruebas del laboratorio 3 fueron exitosas.")


if __name__ == "__main__":
    ejecutar_pruebas()
