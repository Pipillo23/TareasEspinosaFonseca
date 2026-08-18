"""
Módulo con funciones para filtrado de strings y cálculo de extremos.

Este archivo contiene las soluciones solicitadas para la Tarea 1.
"""


def filtrar_vocales(cadena, bandera):
    """
    Filtra una cadena de texto devolviendo solo vocales o consonantes.

    Parámetros:
    -----------
    cadena : str
        El texto de entrada que debe contener únicamente letras alfabéticas.
    bandera : bool
        Si es True, extrae vocales. Si es False, extrae consonantes.

    Retorna:
    --------
    tuple : (código_estado, resultado_string)
        -código_estado (int): 0 en éxito, o un código de error negativo.
        -resultado_string (str u None): El string filtrado o None si hay error
    """
    # 1. Verificar que la cadena sea un string
    if not isinstance(cadena, str):
        return -100, None

    # 2. Verificar que no sea un string vacío
    if len(cadena) == 0:
        return -300, None

    # 3. Verificar que solo contenga letras del abecedario
    if not cadena.isalpha():
        return -200, None

    # 4. Verificar que la longitud no supere los 30 caracteres
    if len(cadena) > 30:
        return -400, None

    # 5. Verificar que bandera sea de tipo booleano estrictamente
    if type(bandera) is not bool:
        return -500, None

    # Definición de conjunto de vocales
    vocales = set("aeiouAEIOU")

    # Filtrado según el estado de la bandera
    if bandera:
        resultado = "".join([c for c in cadena if c in vocales])
    else:
        resultado = "".join([c for c in cadena if c not in vocales])

    return 0, resultado


def encontrar_extremos(lista_numeros):
    """
    Encuentra los valores mínimo y máximo de una lista de números.

    Parámetros:
    -----------
    lista_numeros : list
        Lista que contiene valores numéricos (int o float).

    Retorna:
    --------
    tuple : (código_estado, mínimo, máximo)
        - código_estado (int): 0 en éxito, o un código de error negativo.
        - mínimo (int/float u None): El valor mínimo encontrado o None.
        - máximo (int/float u None): El valor máximo encontrado o None.
    """
    # 1. Verificar que el parámetro sea una lista
    if not isinstance(lista_numeros, list):
        return -600, None, None

    # 2. Verificar que la lista no esté vacía
    if len(lista_numeros) == 0:
        return -800, None, None

    # 3. Verificar que no exceda de 15 elementos
    if len(lista_numeros) > 15:
        return -900, None, None

    # 4. Verificar que todos los elementos sean números (int o float)
    #    Se verifica type(elem) is not bool porque bool hereda de int en Python
    for elem in lista_numeros:
        if type(elem) is bool or not isinstance(elem, (int, float)):
            return -700, None, None

    # Cálculo del valor mínimo y máximo
    val_min = min(lista_numeros)
    val_max = max(lista_numeros)

    return 0, val_min, val_max
