'''Ejercicio triangulo espacios con asteriscos'''

altura = int(input("Introduzca la altura del triangulo "))

print(" " * (altura), end="")
print("*")
for i in range(1, (altura+1)):
    print(" " * (altura - i), end="")
    print("*", end="")
    print(" " * (i-1), end="")
    print("*")

for j in range(altura, 1, -1):
    print(" " * ((altura - j)+1), end="")
    print("*", end="")
    print(" " * (j - 2), end="")
    print("*")
print(" " * (altura), end="")
print("*")





