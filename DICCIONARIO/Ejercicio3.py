frutas = {
    "Platano" : 1.35,
    "Manzana" : 0.80,
    "Pera" : 0.85,
    "Naranja" : 0.70
}

fr = input("Di la fruta: ")
kg = float(input ("Di el nº de kilos: "))

if fr in frutas:
    precio = round(frutas[fr]*kg, 3)
    print (kg, " kilos de ", fr, " cuestan ", precio, "€")
else:
    print ("La fruta no está")