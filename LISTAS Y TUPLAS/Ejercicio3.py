asignaturas = ("Matematicas", "Lengua", "Fisica", "Quimica", "Historia")
a = 0
while a < len(asignaturas):
    nota = input("Que nota has sacado en: "+ asignaturas[a]+" ")
    print ("En ", asignaturas[a], " has sacado un: ", nota)
    a=a+1