'''Programa que suma independientemente los pares y los impares de los números
comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas'''
sumaPar = 0
sumaImpar = 0

for i in range(100, 201):
    if i%2==0:
        sumaPar += i
    else:
        sumaImpar += i

print(f"La suma de los números pares es: {sumaPar}")
print(f"La suma de los números impares es: {sumaImpar}")
    