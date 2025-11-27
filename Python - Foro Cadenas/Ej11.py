'''Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.'''

nueva_cadena = ""
palabra = input("Introduzca una palabra ")

for letra in palabra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        nueva_cadena = nueva_cadena + letra * (2)
    else:
        nueva_cadena += letra
        
print("Su nueva palabra es " + nueva_cadena)
