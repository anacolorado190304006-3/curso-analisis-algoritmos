"""Generadores de datos para el Laboratorio 1."""
import random

def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera n indices de riesgo distintos en orden aleatorio.

    Args:
        n: cantidad de indices de riesgo.
        semilla: semilla para reproducir el resultado.

    Returns:
        Lista de n indices de riesgo distintos.
    """
    generador = random.Random(semilla)
    return generador.sample(range(1, n + 1), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera una lista casi ordenada en orden descendente.

    El 98 % de los datos queda ordenado y el 2 % restante
    se coloca al final en un orden diferente.
    """
    generador = random.Random(semilla)
    cantidad_nuevos = max(2, round(n * 0.02))
    cantidad_ordenada = n - cantidad_nuevos
    datos = list(range(n, 0, -1))
    parte_ordenada = datos[:cantidad_ordenada]
    nuevos = datos[cantidad_ordenada:]
    generador.shuffle(nuevos)
    return parte_ordenada + nuevos

def generar_inverso(n: int) -> list[int]:
    """Genera una lista en orden ascendente, inverso al requerido.

    Args:
        n: cantidad de indices de riesgo.

    Returns:
        Lista de n indices de riesgo en orden ascendente.
    """
    return list(range(1, n + 1))
