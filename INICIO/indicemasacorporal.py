peso=float(input("Di tu peso en Kilogramos: "))
altura=float(input("Di tu altura en metros"))

print("Tu indice de masa corporal es: " + str(round((peso/altura**2), 2)))