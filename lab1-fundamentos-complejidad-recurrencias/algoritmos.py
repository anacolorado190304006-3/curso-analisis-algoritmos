def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arreglo = datos.copy()
    comparaciones = 0

    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if arreglo[j] < clave:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            else:
                break
        arreglo[j + 1] = clave
    return arreglo, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.
    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    if len(datos) <= 1:
        return datos.copy(), 0

    mitad = len(datos) // 2
    izquierda, comparaciones_izquierda = merge_sort(datos[:mitad])
    derecha, comparaciones_derecha = merge_sort(datos[mitad:])
    resultado = []
    i = 0
    j = 0
    comparaciones = comparaciones_izquierda + comparaciones_derecha

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado, comparaciones
