cantidad=float(input("Di la cantidad a invertir: "))
interes=float(input("Di el interes anual:"))
anios=int(input("Di cuantos años:"))

print ("El capital obtenido es: " + str(cantidad*(interes/100)*anios))