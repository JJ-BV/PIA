# Problema 3. Trabajo con conjuntos
# Escribe una función que reciba dos listas de enteros y devuelva un diccionario
# con la siguiente información (ES OBLIGATORIO USAR CONJUNTOS PARA CALCULARLOS)
# 1. La intersección de ambos conjuntos (elementos comunes).
# 2. La unión de ambos conjuntos (todos los elementos sin duplicados).
# 3. La diferencia simétrica (elementos que están en uno u otro conjunto,
# pero no en ambos).


def myFunction (listA, listB):
    # 1. La intersección de ambos conjuntos (elementos comunes).
    # elementos comunes de A y B
    listABIntersection = listA.intersection(listB) 
    # 2. La unión de ambos conjuntos (todos los elementos sin duplicados).
    listABUnion = listA.union(listB)
    # 3. La diferencia simétrica (elementos que están en uno u otro conjunto, pero no en ambos).
    # diferencia simétrica: elementos de A que no están en B
    listDifAB = listA.difference(listB)
    # diferencia simétrica: elementos de B que no están en A
    listDifBA = listB.difference(listA)

    result = {
        'intersection' : listABIntersection,
        'union': listABUnion,
        'simetricDiff': {
            'AB': sorted(listDifAB),
            'BA': sorted(listDifBA)
        }
        }
    for k, v in result.items():
        print(f"{k} --> {v}")

# dos formar de crear conjuntos
listA = set([0,1,2,3,4,5])
listB = {0,4,5,6,7,8,9}

myFunction(listA, listB)