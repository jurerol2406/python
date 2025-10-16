edad = int(input("Di tu edad: "))
ingreso = int(input("Di cuanto ingresas mensualmente: "))

if edad > 18 and ingreso > 1000:
    print ("Tienes que tributar")
else:
    print ("No tienes que tributar")