def calcular_promedio(lista: list[int]) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        lista: Lista de números enteros.

    Returns:
        El promedio de los números de la lista.
    """
    suma = 0

    for numero in lista:
        suma = suma + numero
    
    return suma / len(lista)


def main() -> None:
    """Ejecuta el cálculo del promedio con una lista de ejemplo."""
    lista_ejemplo = [1, 2, 3, 4, 5]
    print(calcular_promedio(lista_ejemplo))


if __name__ == "__main__":
    main()