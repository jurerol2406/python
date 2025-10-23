num = int(input("Di una cantidad a invertir: "))
interes = int(input("Di el interes anual: "))
anio = int (input("Di cuantos años: "))

for x in range (0, anio+1):
    capital = num * (1 + interes/100) ** x
    print ("Se ha obtenido un capital de ", capital, " en el año ", x)