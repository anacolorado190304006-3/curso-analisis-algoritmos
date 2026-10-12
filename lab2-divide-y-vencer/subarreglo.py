
"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(
    valores: list[float],
) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias.

    Args:
        valores: Variacion diaria de caja. Tiene al menos un elemento.

    Returns:
        Tupla (inicio, fin, suma), con indices inclusivos y suma maxima.
    """
    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = float("-inf")

    for inicio in range(len(valores)):
        suma = 0.0

        for fin in range(inicio, len(valores)):
            suma += valores[fin]

            if suma > mejor_suma:
                mejor_inicio = inicio
                mejor_fin = fin
                mejor_suma = suma

    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: Variacion diaria de caja.
        inicio: Indice inicial del rango, inclusive.
        medio: Ultimo indice de la mitad izquierda.
        fin: Indice final del rango, inclusive.

    Returns:
        Tupla (inicio, fin, suma) del mejor tramo cruzado.
    """
    suma = 0.0
    mejor_suma_izquierda = float("-inf")
    mejor_inicio = medio

    for i in range(medio, inicio - 1, -1):
        suma += valores[i]

        if suma > mejor_suma_izquierda:
            mejor_suma_izquierda = suma
            mejor_inicio = i

    suma = 0.0
    mejor_suma_derecha = float("-inf")
    mejor_fin = medio + 1

    for j in range(medio + 1, fin + 1):
        suma += valores[j]

        if suma > mejor_suma_derecha:
            mejor_suma_derecha = suma
            mejor_fin = j

    return (
        mejor_inicio,
        mejor_fin,
        mejor_suma_izquierda + mejor_suma_derecha,
    )


def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha mediante divide y venceras.

    Args:
        valores: Variacion diaria de caja.
        inicio: Indice inicial del rango, inclusive.
        fin: Indice final del rango, inclusive.

    Returns:
        Tupla (inicio, fin, suma) del mejor tramo encontrado.
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    resultado_izquierda = subarreglo_maximo(
        valores, inicio, medio
    )
    resultado_derecha = subarreglo_maximo(
        valores, medio + 1, fin
    )
    resultado_cruzado = suma_cruzada(
        valores, inicio, medio, fin
    )

    if (
        resultado_izquierda[2] >= resultado_derecha[2]
        and resultado_izquierda[2] >= resultado_cruzado[2]
    ):
        return resultado_izquierda

    if resultado_derecha[2] >= resultado_cruzado[2]:
        return resultado_derecha

    return resultado_cruzado