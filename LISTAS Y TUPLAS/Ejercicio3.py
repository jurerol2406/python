asignaturas = ("Matematicas", "Lengua", "Fisica", "Quimica", "Historia")
a = 0
notas = []
while a < len(asignaturas):
    nota = input("Que nota has sacado en: "+ asignaturas[a]+" ")
    notas.append(nota)
    a=a+1
for i in range(len(asignaturas)):
    print ("En ", asignaturas[i], " has sacado un: ", notas[i])