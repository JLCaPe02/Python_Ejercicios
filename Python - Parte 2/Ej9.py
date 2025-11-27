'''Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos.'''

n = int(input("Introduzca un número mayor a cero "))

contadorPos = 0
contadorNeg = 0

while n < 0:
    n = int(input("Introduzca un número mayor a cero "))

while n != 0:
    if n > 0:
        contadorPos += 1
    else:
        contadorNeg += 1
    n = int(input("Introduzca un número mayor a cero "))

if (contadorNeg > 1):
    print(f"Se han encontrado {contadorNeg} números negativos")
else: 
    print("No se han encotrado números negativos")

if (contadorPos > 1):
    print(f"Se han encontrado {contadorPos} números positivos")
else: 
    print("No se han encotrado números positivos")
        