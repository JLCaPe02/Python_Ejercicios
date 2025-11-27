'''Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes (sin listas, usando condiciones y concatenación).'''

cadena = input("Introduzca una cadena de caracteres ")
nueva_cadena = ""
for letra in cadena:
    if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        nueva_cadena += letra

print(f"Su nueva cadena con solo las consonantes es {nueva_cadena}")