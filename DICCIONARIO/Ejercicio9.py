Facturas ={}
opcion = 0
cobrar = 0
cobrado = 0
while opcion != 3:
    print ("1. Nueva factura")
    print ("2. Pagar factura existente")
    print ("3. Salir")
    opcion=int(input("Que opción quieres hacer: "))
    if opcion == 1:
        nfactura=int(input("Di el numero de la factura"))
        pfactura=float(input("Di cuanto es el precio de la factura"))
        Facturas[nfactura] = pfactura
        cobrar = cobrar+pfactura
    elif opcion == 2:
        for i in Facturas.items():
            print(i)
        pagar=int(input("Que factura quieres pagar, di el numero de la factura"))
        coste = Facturas.pop(pagar)
        cobrado = cobrado + pfactura
        cobrar = cobrar - pfactura
    elif opcion > 3:
        print ("OPCIÓN NO VÁLIDA")
    print ("Cobrado: ", cobrado)
    print ("Pendiente de cobro: ", cobrar )
    


