asignaturas = ("Matemáticas", "Física", "Química", "Historia", "Lengua")
notas = []
a = 0
while a < len(asignaturas):
    nota = input("Que nota has sacado en: "+ asignaturas[a]+" ")
    notas.append(nota)
    a=a+1

asignaturas = [asignaturas[i]for i in range(len(asignaturas)) if int(notas[i]) < 5]
print ("Tienes que repetir: ", asignaturas)    
