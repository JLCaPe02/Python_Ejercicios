'''Programa que lee una secuencia de notas (con valores que van de 0 a 10) que termina con
el valor -1 y nos dice si hubo o no alguna nota con valor 10.'''

n = int(input("Introduzca una nota positiva o nula "))
flag = 0
while n < 0:
    n = int(input("Introduzca una nota positiva o nula "))

while n != -1:
    if n == 10:
        flag += 1
    n = int(input("Introduzca una nota positiva o nula "))
if flag > 0:
    print("Ha habido nota/s con valor a 10")
else:
    print("No ha habido ningún 10 entre las notas")