nombre = input ("Di tu nombre: ")
sexo = input ("Di tu sexo: ")

nom=nombre.lower()

inicial = nom [0]


if (inicial <= "m" and sexo == "mujer") or (inicial >= "n" and sexo == "hombre"):
    print ("Es del grupo A")
else:
    print ("Es del grupo B")
