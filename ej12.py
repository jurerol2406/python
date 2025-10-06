barras = float(input("¿Cuántas barras no son del dia?: "))
precio = 3.49
descuento = (precio*barras*0.6)
total=(precio*barras)-descuento
print ("Las barras habitualmente cuestan 3,49€, se le va a hacer un descuento de ", round((3.49*0.6),2), "€ por cada barra, un descuento total de "+ str(descuento) + "€ asi que costará ", round(total, 2), "€")