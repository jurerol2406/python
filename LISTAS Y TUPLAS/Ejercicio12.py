# Matrices
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

resultado = [
    [0, 0],
    [0, 0]
]

for i in range(2): 
    for j in range(2):
        for k in range(3):
            resultado[i][j] += matriz[i][k] * matriz2[k][j]

print("El resultado de las matrices es:")
for fila in resultado:
    print(fila)
