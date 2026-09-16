"""Experimento de la Parte 3 del Laboratorio 1."""

import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

def medir_insertion(datos: list[int]) -> tuple[float, int]:
    """Mide el tiempo y las comparaciones de insertion sort.

    Args:
        datos: lista de indices de riesgo que se va a ordenar.

    Returns:
        Tupla con el tiempo promedio en segundos y las comparaciones.
    """
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)
    tiempo_promedio = sum(tiempos) / REPETICIONES
    return tiempo_promedio, comparaciones


def ejecutar_experimento() -> None:
    """Ejecuta las mediciones y genera las graficas de la Parte 3."""
    resultados = {
        "A - Aleatorio": {"tiempo": [], "comparaciones": []},
        "B - Casi ordenado": {"tiempo": [], "comparaciones": []},
        "C - Inverso": {"tiempo": [], "comparaciones": []},
    }

    print("Parte 3 - Casos de entrada")
    print()
    for n in TAMANOS:
        datos_a = generar_aleatorio(n)
        datos_b = generar_casi_ordenado(n)
        datos_c = generar_inverso(n)

        tiempo_a, comparaciones_a = medir_insertion(datos_a)
        tiempo_b, comparaciones_b = medir_insertion(datos_b)
        tiempo_c, comparaciones_c = medir_insertion(datos_c)

        resultados["A - Aleatorio"]["tiempo"].append(tiempo_a)
        resultados["A - Aleatorio"]["comparaciones"].append(
            comparaciones_a
        )

        resultados["B - Casi ordenado"]["tiempo"].append(tiempo_b)
        resultados["B - Casi ordenado"]["comparaciones"].append(
            comparaciones_b
        )

        resultados["C - Inverso"]["tiempo"].append(tiempo_c)
        resultados["C - Inverso"]["comparaciones"].append(
            comparaciones_c
        )

        print(f"n = {n}")
        print(
            f"A - Aleatorio: "
            f"tiempo promedio = {tiempo_a:.6f} s, "
            f"comparaciones = {comparaciones_a}"
        )
        print(
            f"B - Casi ordenado: "
            f"tiempo promedio = {tiempo_b:.6f} s, "
            f"comparaciones = {comparaciones_b}"
        )
        print(
            f"C - Inverso: "
            f"tiempo promedio = {tiempo_c:.6f} s, "
            f"comparaciones = {comparaciones_c}"
        )
        print()
    generar_grafica_comparaciones(resultados)
    generar_grafica_tiempo(resultados)


def generar_grafica_comparaciones(resultados: dict) -> None:
    """Genera la grafica de comparaciones frente al tamaño."""
    for escenario, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["comparaciones"],
            marker="o",
            label=escenario,
        )
    plt.title("Insertion Sort: comparaciones por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()


def generar_grafica_tiempo(resultados: dict) -> None:
    """Genera la grafica de tiempo frente al tamaño."""
    for escenario, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["tiempo"],
            marker="o",
            label=escenario,
        )
    plt.title("Insertion Sort: tiempo de ejecución por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


if __name__ == "__main__":
    ejecutar_experimento()