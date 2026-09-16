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
