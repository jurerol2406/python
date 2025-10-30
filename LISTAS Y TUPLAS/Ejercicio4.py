loteria = input ("Di los números de la loteria separados por COMAS (,): ")
lista = loteria.split(",")

listaordenada = sorted(lista, reverse=True)
print (listaordenada)