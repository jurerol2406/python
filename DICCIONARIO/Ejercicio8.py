dicc = dict()
cuantas = input("Cuantas palabras quieres tener en el diccionario: ")
for i in range (1, cuantas):
    palabras = input("Di las palabras con el formato de español:ingles: ")
    separar = palabras.split(":")
    español = separar[0]
    ingles = separar[1]
    dicc[español] = ingles
frase = input("Di una frase que se traduzca con las palabras del diccionario: ")
