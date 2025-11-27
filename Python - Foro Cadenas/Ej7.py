'''Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.'''
nueva_cadena = ""
cadena = input("Introduzca una palabra ")
caracter = input("Introduzca el carácter a reemplezar en su palabra ")
caracter_nuevo = input("Introduzca un carácter nuevo para reemplezar por el caracter anterior ")


for letra in cadena:
    if letra == caracter:
        nueva_cadena += caracter_nuevo
    else:
        nueva_cadena += letra
    
    
print(f"Su nueva palabra es {nueva_cadena}")