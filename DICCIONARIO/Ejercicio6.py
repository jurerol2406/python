dicc = dict()
elementos = int(input("Cuantos quieres añadir al diccionario: "))
for i in range(1,elementos+1):
    titulo = input("Di el titulo del objeto: ")
    valor = input ("Di el valor para ese objeto")
    dicc [titulo] = valor
    print (dicc)