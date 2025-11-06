curso = {
    "Matematicas":6,
    "Fisica":4,
    "Quimica":5
}
totalcreditos = 0
for asignatura, creditos in curso.items():
    print (asignatura, " tiene ", creditos, " creditos")
    totalcreditos = totalcreditos+creditos
print ("El numero total de creditos es: ", totalcreditos)