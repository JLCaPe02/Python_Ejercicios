'''Imprime la letra M mayúscula usando asteriscos en una matriz cuadrada de tamaño impar n. Las líneas de la M deben visualizarse usando asteriscos, con espacios en el resto.

Figura para n=7:'''

n = int(input("Escriba la altura para la letra mayúscula "))
mitad = n//2 + 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (j==1 or j==n):
            print("*", end="")
        elif (j==i or j + i == n + 1) and i<=mitad:
            print("*", end="")
        else:
            print(" ", end="")
    print()