asignaturas = ("Matemáticas", "Física", "Química", "Historia", "Lengua")
notas = []
a = 0
while a < len(asignaturas):
    nota = input("Que nota has sacado en: "+ asignaturas[a]+" ")
    notas.append(nota)
    a=a+1

for i in range(len(asignaturas)):
    if str(notas[i]) < 5:
        asignaturas = [asignaturas[i]]
print ("Tienes que repetir: ", asignaturas)    
