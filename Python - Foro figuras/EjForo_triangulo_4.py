'''Triangulo con 4 y huecos'''

altura = int(input("Introduzca la altura del triangulo"))
print("4")
for i in range(1, altura -1):
    print(f"{altura} ", end="")
    print("  " * (i-1), end="")
    print(f"{altura} ",)

print("4 " * altura)
