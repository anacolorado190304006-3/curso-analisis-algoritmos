
"""Mide y compara los algoritmos de subarreglo maximo."""

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


TAMANOS = [10, 50, 100, 200, 500, 1000, 2000, 4000]
REPETICIONES = 3
SEMILLA = 42


def medir_tiempo(funcion, valores: list[int]) -> float:
    """Calcula el tiempo mediano de ejecucion de un algoritmo.

    Args:
        funcion: Algoritmo que recibe una lista y devuelve una tupla.
        valores: Lista de variaciones diarias de caja.

    Returns:
        Tiempo mediano de ejecucion en segundos.
    """
    tiempos = []

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        resultado = funcion(valores)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return statistics.median(tiempos)


def ejecutar() -> None:
    """Mide ambos algoritmos y guarda la grafica comparativa."""
    generador = random.Random(SEMILLA)
    tiempos_bruta = []
    tiempos_divide = []

    for n in TAMANOS:
        valores = [generador.randint(-100, 100) for _ in range(n)]

        def fuerza_bruta(datos: list[int]) -> tuple[int, int, float]:
            return subarreglo_fuerza_bruta(datos)

        def divide_y_venceras(
            datos: list[int],
        ) -> tuple[int, int, float]:
            return subarreglo_maximo(datos, 0, len(datos) - 1)

        suma_bruta = subarreglo_fuerza_bruta(valores)[2]
        suma_divide = subarreglo_maximo(
            valores, 0, len(valores) - 1
        )[2]
        assert suma_bruta == suma_divide, (
            f"Los resultados no coinciden para n={n}"
        )

        tiempo_bruta = medir_tiempo(fuerza_bruta, valores)
        tiempo_divide = medir_tiempo(divide_y_venceras, valores)

        tiempos_bruta.append(tiempo_bruta)
        tiempos_divide.append(tiempo_divide)

        print(
            f"n={n:4d} | Fuerza bruta: {tiempo_bruta:.6f} s"
            f" | Divide y venceras: {tiempo_divide:.6f} s"
        )

    plt.figure(figsize=(10, 6))
    plt.plot(TAMANOS, tiempos_bruta, marker="o", label="Fuerza bruta O(n²)")
    plt.plot(
        TAMANOS,
        tiempos_divide,
        marker="s",
        label="Divide y venceras O(n log n)",
    )
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Tamaño de entrada n (elementos, escala logarítmica)")
    plt.ylabel("Tiempo mediano (segundos, escala logarítmica)")
    plt.title("Comparación de algoritmos de subarreglo máximo")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.4)
    plt.tight_layout()

    carpeta = Path(__file__).parent / "graficas"
    carpeta.mkdir(parents=True, exist_ok=True)
    ruta = carpeta / "tiempo_vs_n.png"
    plt.savefig(ruta, dpi=200)
    plt.close()

    print(f"\nGrafica guardada en: {ruta}")


if __name__ == "__main__":
    ejecutar()