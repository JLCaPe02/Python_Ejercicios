'''Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'.'''

nueva_cadena =""
cadena = input("Introduzca una cadena de caracteres o palabra ")

for letra in cadena:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        nueva_cadena += '*'
    else:
        nueva_cadena += letra

print(f"Su cadena de caracteres con asteriscos en las vocales es {nueva_cadena}")