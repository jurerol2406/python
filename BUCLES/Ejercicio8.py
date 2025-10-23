num = int(input("Di un número: "))

for x in range (1, num+1):   
    if x % 2 == 1:
        espacio = ""
        for i in range (x, 0, -2):
            espacio += str(i)+ ""
        print (espacio)