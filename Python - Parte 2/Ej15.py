'''Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos
la altura de la pirámide por teclado. Este es un ejemplo:'''

altura = int(input("Introduzca la altura del triángulo invertido"))

for i in range(altura,0,-1):
    print(" " * (altura-i), end="")
    print("*" * ((i*2) -1))