numero = input ("Di los números separados por COMAS (,): ")
lista = numero.split(",")

suma = 0
for i in range(len(lista)):
    suma = suma + int(lista[i])

media = suma/len(lista)

for i in numero:
    sumacuadrado = suma + ((i) - int(media))**2
desviacion = (sumacuadrado / len(lista))**0.5

print ("La media es: ", media)
print ("La desviación tipica es: ", desviacion)

