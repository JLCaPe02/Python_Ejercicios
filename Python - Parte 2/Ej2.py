'''Programa que muestre los números pares comprendidos entre el 1 y el 200. Para ello utiliza
un contador y suma de 2 en 2.'''

contador = 0
for i in range(0, 200, 2):
    if (i%2==0):
        contador += 1

print(f"El total de números pares entre el 1 y el 200 es de {contador} números")