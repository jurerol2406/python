num = int(input("Di un número: "))
divisores = 0
for x in range (1, num):
    if num % x == 0:
        divisores = divisores + 1

if divisores > 2:
    print (num, "no es primo")
else:
    print (num, "es primo")