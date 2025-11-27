'''Programa que muestre los números pares comprendidos entre el 1 y el 200. Esta vez utiliza
un contador sumando de 1 en 1.'''
contador = 0
for i in range(1, 201):
    if (i%2==0):
        contador += 1

print(f"El total de números pares entre el 1 y el 200 es de {contador} números")