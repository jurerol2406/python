palabra = input("Di una palabra para comprobar si es palindromo: ").lower()
lista = list(palabra)
listareversa = list(lista)
listareversa.reverse()

if lista == listareversa:
    print (palabra, "es palindromo")
else:
    print (palabra, " no es palindromo")