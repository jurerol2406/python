dinero = float(input("¿Cuánto dinero ha depositado?: "))

print("El primer año:", round(dinero * 1.04, 2))
print("El segundo año:", round(dinero * 1.04**2, 2))
print("El tercer año:", round(dinero * 1.04**3, 2))