'''Programa que muestre los números desde el 1 hasta un número N que se introducirá por
teclado.'''

n = int(input("Introduzca un número cualquiera que sea mayor a cero "))
while n <= 0:
    n = int(input("Introduzca un número cualquiera que sea mayor a cero "))
    
for i in range(1, n + 1):
    print(i)