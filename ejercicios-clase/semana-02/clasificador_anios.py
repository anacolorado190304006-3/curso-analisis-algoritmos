"""Clasificador de años bisiestos.
 
Complete las funciones siguiendo la especificación de cada docstring.
"""
 
 
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
 
 
def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    while True:
        try:
            print('-------------- CLASIFICADOR DE AÑOS --------------')
            lista = input('Ingrese la lista de años separados por comas (ej. 2000, 2023, 2024): ')
            anios = [int(anio.strip()) for anio in lista.split(",")]

            if any(anio < 0 for anio in anios):
                raise ValueError(f"Los años no pueden ser negativos")

            return anios
        except ValueError as error:
            print(f'ERROR: {error}, verifique los valores ingresados\n')
 
 
def main() -> None:
    """Punto de entrada del script."""
    lista_anio = leer_anios()
    bisiesto = [anio for anio in lista_anio if es_bisiesto(anio)]

    decadas = {anio // 10 * 10 for anio in lista_anio}

    agrupados = {
        decada: [anio for anio in lista_anio if anio // 10 * 10 == decada]
        for decada in decadas
    }

    print(f"\n→ Años ingresados: {lista_anio}")
    print(f"→ Años agrupados por década: {agrupados}\n")
    print(" ----------------- RESULTADO ----------------- ")
    print(f"→ Años bisiestos: {bisiesto}")
    print(f"→ Cantidad de años bisiestos: {len(bisiesto)} de {len(lista_anio)}")
 
 
if __name__ == "__main__":
    main()