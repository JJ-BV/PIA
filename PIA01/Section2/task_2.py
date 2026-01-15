# Problema 2. Frecuencia de palabras en un texto.
# Escribe una función que reciba por parámetro una lista de palabras y la ruta a
# un fichero de texto y devuelva un diccionario que muestre cuantas veces
# aparecen las disƟntas palabras de la lista en el fichero de texto. Haz un pequeño
# programa que la ponga a prueba.
# Requisitos:
# 1. Eliminar signos de puntuación y convertir todo a minúsculas.
# 2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia.
# 3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.


import string

def wordCount(words, path):
    # Leer el archivo
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    # 1. Eliminamos signos de puntuación y convertir todo a minúsculas.
    # hace falta importar librería string
    translator = str.maketrans('', '', string.punctuation)
    content = content.translate(translator).lower()
    
    # Dividimos en palabras
    wordslist = content.split()
    
    # Eliminamos signos de puntuación de las palabras de entrada y convertirmos a minúsculas
    cleaned_words = [word.translate(translator).lower() for word in words]
    
    # Iniciamos el diccionario (sin puntuación y en minúsculas)
    wordDict = {cleaned_word: 0 for cleaned_word in cleaned_words}
    
    # 2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia.
    for word in wordslist:
        if word in wordDict:
            wordDict[word] += 1
    
    return wordDict


result = wordCount(['ipsum', 'amet,', 'dolor,'], './task_2_file_example.txt')

# 3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.
for word in sorted(result.keys()):
    print(f"'{word}' aparece: {result[word]} veces")

# Test. Recuento a mano:
# ipsum : 2
# amet, : 3
# dolor : 3