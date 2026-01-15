# Problema 1. Procesamiento de una lista de enteros.
# Crea una función que reciba una lista de enteros por parámetro y devuelva otra
# lista, de acuerdo a las siguientes acciones:
# 1. Eliminar los números negativos de la lista.
# 2. Eliminar los valores que están repetidos, quedándonos con uno de ellos.
# 3. Ordenar los números resultantes de menor a mayor.
# Por ejemplo, si le pasara [4, -1, 2, 4, 3, -5, 2], debería retornar [2,3,4].


def process_list(lst):
    #1. Eliminar los números negativos de la lista. 
    # He usado la expresión de bucle en una línea
    filteredList = [n for n in lst if n > 0]
    #2. Eliminar los valores que están repetidos
    uniqueList = list(dict.fromkeys(filteredList))
    #3. Ordenar los números resultantes de menor a mayor.
    uniqueList.sort()
    return uniqueList

print(process_list([4, -1, 2, 4, 3, -5, 2]))