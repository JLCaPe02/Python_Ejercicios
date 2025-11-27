'''Programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos
son positivos y cuantos negativos.'''

contadorPos = 0
contadorNeg = 0

n = int(input("Introduzca un número "))
for i in range(n, n + 100):
    if (i < 0):
        contadorNeg += 1
    else:
        contadorPos += 1


print(f"Se han leído {contadorPos} números positivos")
print(f"Se han leído {contadorNeg} números negativos")

