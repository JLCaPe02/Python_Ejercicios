'''Crea una aplicación que dibuje una escalera de números, siendo cada línea números
empezando en uno y acabando en el numero de la línea. Este es un ejemplo, si introducimos un
5 como altura'''

num = int(input("Introduzca un número para que sea la altura de la escalera "))

for i in range(1, num +1):
    contador = 0
    for j in range(0, i):
        contador += 1
        print(contador, end="")
    print()   