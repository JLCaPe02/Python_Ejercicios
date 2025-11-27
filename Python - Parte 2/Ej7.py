'''Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún
número negativo o no.'''

contador = 0

n = int(input("Introduzca un número "))
for i in range(n, n + 100):
    if (i < 0):
        contador += 1

if contador > 0:
    print(f"Se han leído {contador} números negativos")
else:
    print("No han habido números negativos")