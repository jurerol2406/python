frase = input("Di una frase: ")
letra = input("Di una letra para contar las veces que aparece: ")
a = 0
contador = 0
frasefor = frase.lower()
while a < len(frasefor):
    if frasefor[a] == letra:
        contador = contador+1
    a=a+1
print (contador)