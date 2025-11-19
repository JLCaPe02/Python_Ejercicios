'''Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de
la escalera por teclado. Este es un ejemplo si insertaras un 5 de altura:'''

altura = int(input("Introduzca la altura de la escalera "))
asterisco = "*"

for i in range(1,altura+1):
    for j in range(0,i):
        print(asterisco,end="")
    print()