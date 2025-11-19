'''Crea una aplicación que dibuje una escalera de números, siendo cada línea un número.
Nosotros le pasamos la altura por teclado.'''

num = int(input("Introduzca un número para que sea la altura de la escalera "))

for i in range(1, num +1):
    contador = i
    for j in range(0, i):
        print(contador, end="")
    print()   