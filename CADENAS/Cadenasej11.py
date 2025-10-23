producto = input("Di el nombre del producto: ")
precio = float(input ("Di el precio del producto: "))
numero= float(input ("Di el número de unidades del producto: "))

unitario = f"{precio:09.2f}"
unidades = f"{numero:03.0f}"
coste = precio*numero
total = f"{coste:011.2f}"

print ("El producto ", producto, " tiene un precio unitario de ", unitario, " se han pedido ", unidades,
       " unidades, asi que tendra un coste total de ", total, " €")
