palabra = input ("Di una palabra: ")
a = 0
i=len(palabra)
while a < len(palabra):
    print (palabra[::-a])
    a = a+1
