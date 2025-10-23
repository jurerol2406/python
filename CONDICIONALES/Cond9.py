edad = int(input("Di tu edad: "))
if edad < 4:
    print ("Entrada gratis")
elif edad >= 4 and edad <= 18:
    print ("La entrada cuesta 5€")
elif edad > 18:
    print ("La entrada cuesta 10€")