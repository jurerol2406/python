asignaturas = ("Matemáticas", "Física", "Química", "Historia", "Lengua")
notas = []
a = 0
while a < len(asignaturas):
    nota = input("Que nota has sacado en: "+ asignaturas[a]+" ")
    notas.append(nota)
    a=a+1

for i in range(len(asignaturas)):
    if int(notas[i]) < 5:
        print ("En ", asignaturas[i], " has sacado un: ", notas[i], " tienes que repetir la asginatura")