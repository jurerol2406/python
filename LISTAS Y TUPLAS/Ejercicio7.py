
abecedario = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

abecedario = [abecedario[i] for i in range(len(abecedario)) if (i+1) % 3 != 0 or i == 0]
              
print (abecedario)