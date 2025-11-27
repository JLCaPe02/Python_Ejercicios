'''Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado. Este es un ejemplo, si introducimos 5 de altura'''

altura = int(input("Introduzca altura de la pirámide "))

for l in range(1, altura + 1):
    print(" " * (altura - l), end="")
    print("*" * ((l*2) - 1))
    