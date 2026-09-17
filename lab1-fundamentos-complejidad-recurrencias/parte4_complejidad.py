"""Comparacion experimental entre insertion sort y merge sort."""

import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

def medir_algoritmo(algoritmo, datos: list[int]) -> float:
    """Mide el tiempo promedio de ejecucion de un algoritmo."""
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(datos)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return sum(tiempos) / len(tiempos)


def ejecutar_experimento() -> None:
    """Compara los tiempos de insertion sort y merge sort."""
    resultados_insertion = []
    resultados_merge = []
    print("Parte 4 - Comparacion de algoritmos")

    for n in TAMANOS:
        datos = generar_aleatorio(n)

        tiempo_insertion = medir_algoritmo(insertion_sort, datos)
        tiempo_merge = medir_algoritmo(merge_sort, datos)

        resultados_insertion.append(tiempo_insertion)
        resultados_merge.append(tiempo_merge)

        print(f"\nn = {n}")
        print(
            f"Insertion sort: {tiempo_insertion:.6f} s"
        )
        print(
            f"Merge sort:     {tiempo_merge:.6f} s"
        )

    generar_grafica(
        resultados_insertion,
        resultados_merge,
    )
    

def generar_grafica(resultados_insertion: list[float], resultados_merge: list[float]) -> None:
    """Genera la grafica de tiempos de ambos algoritmos."""
    plt.figure(figsize=(10, 6))

    plt.plot(
        TAMANOS,
        resultados_insertion,
        marker="o",
        label="Insertion sort",
    )

    plt.plot(
        TAMANOS,
        resultados_merge,
        marker="o",
        label="Merge sort",
    )
    plt.title("Comparacion de tiempos de ejecucion")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo promedio (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()

if __name__ == "__main__":
    ejecutar_experimento()