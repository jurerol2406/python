palabra = input("Di una palabra: ").lower()
a = list()
e = list ()
i = list ()
o = list()
u= list()

lista = list(palabra)
a = [letra for letra in palabra if letra == "a"]
e = [letra for letra in palabra if letra == "e"]
i = [letra for letra in palabra if letra == "i"]
o = [letra for letra in palabra if letra == "o"]
u = [letra for letra in palabra if letra == "u"]
print ("La letra (a) aparece ", len(a), " veces")
print ("La letra (e) aparece ", len(e), " veces")
print ("La letra (i) aparece ", len(i), " veces")
print ("La letra (o) aparece ", len(o), " veces")
print ("La letra (u) aparece ", len(u), " veces")