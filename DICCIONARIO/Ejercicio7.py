dicc = dict()
respuesta = 0
total = 0
while respuesta != "si":
    objeto = input("Di el objeto: ")
    coste = int(input ("Di el precio para ese objeto: "))
    dicc [objeto] = coste
    total = total + coste
    respuesta = input("¿Has terminado? (si): ")
print (dicc)
print ( "Total: ", total)