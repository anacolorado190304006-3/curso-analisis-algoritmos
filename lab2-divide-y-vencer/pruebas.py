
"""Pruebas de los algoritmos de subarreglo maximo."""

import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
)


def verificar(valores: list[float]) -> None:
    """Comprueba que ambos algoritmos obtienen la misma suma."""
    copia = valores.copy()

    suma_bruta = subarreglo_fuerza_bruta(valores)[2]
    suma_divide = subarreglo_maximo(
        valores, 0, len(valores) - 1
    )[2]

    assert suma_bruta == suma_divide, (
        f"Resultados diferentes para {valores}: "
        f"{suma_bruta} != {suma_divide}"
    )
    assert valores == copia, "Un algoritmo modifico la lista"


serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

verificar([7])
verificar([-8, -3, -6, -2])
verificar([2, 4, 1, 5])
verificar([1, -10, 4, 5, -1])

# El mejor tramo cruza el punto medio.
cruzado = [1, -10, 4, 5, -1]
assert subarreglo_maximo(
    cruzado, 0, len(cruzado) - 1
)[2] == 9

# Veinte listas aleatorias reproducibles.
generador = random.Random(42)

for _ in range(20):
    longitud = generador.randint(1, 30)
    valores = [
        generador.randint(-20, 20)
        for _ in range(longitud)
    ]
    verificar(valores)

print("Todas las pruebas pasaron correctamente.")