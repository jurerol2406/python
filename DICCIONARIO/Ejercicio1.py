divisas = {"Euro": "€", "Dollar":"$", "Yen":"¥"}
moneda = input ("Di la divisa para mostrar el simbolo: ")

if moneda.title() in divisas:
    print(divisas[moneda.title()])
else:
    print ("La divisa no está")