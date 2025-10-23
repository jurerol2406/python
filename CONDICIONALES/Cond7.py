renta = int(input ("Di tu renta anual: "))

if renta < 10000:
    print ("Tu tipo de impositivo es de 5%")
elif renta > 10000 and renta < 20000:
    print ("Tu tipo de impositivo es de 15%")
elif renta > 20000 and renta < 35000:
    print ("Tu tipo de impositivo es de 20%")
elif renta > 35000 and renta < 60000:
    print ("Tu tipo de impositivo es de 30%")
elif renta > 60000:
    print ("Tu tipo de impositivo es de 45%")