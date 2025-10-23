pizza = input ("¿Pizza vegetariana?: ")
min = pizza.lower()
if min == "si":
    print ("INGREDIENTES PIZZA VEGETARIANA")
    print ("------------------------------")

    print ("Pimiento, Tofu")
    ing = input("Elija 1 de los ingredientes")
    print ("La pizza lleva Tomate, Mozzarella y ", ing)
elif min == "no":
    print ("INGREDIENTES PIZZA NO VEGETARIANA")
    print ("---------------------------------")

    print ("Peperoni, Jamón, Salmón")
    ing = input("Elija 1 de los ingredientes")
    print ("La pizza lleva Tomate, Mozzarella y ", ing)
else:
    print ("Respuesta erronea, debe responder si o no")

