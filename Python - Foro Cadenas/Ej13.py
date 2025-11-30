'''Leer una cadena y eliminar todos los espacios, construyendo una cadena continua.'''
nueva_cadena = ""
cadena = input("Introduzca una cadena de caracteres o palabra ")

for letra in cadena:
    if letra == " ":
        nueva_cadena += ""
    else:
        nueva_cadena += letra

print(f"Su cadena de caracteres sin espacios es {nueva_cadena}")