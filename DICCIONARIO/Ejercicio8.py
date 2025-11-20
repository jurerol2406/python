diccionario = {}
palabras = input("Di las palabras con el formato de español:ingles: ")
for i in palabras.split(","):
    español, ingles = i.split(":")
    diccionario[español] = ingles
frase = input("Di una frase que se traduzca con las palabras del diccionario: ")
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=" ")
    else:
        print(i, end=" ")