'''Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez'''

cadena = input("Introduzca una cadena de caracteres ")
nueva_cadena = ""
contador = 0
for i in range(len(cadena)):
    for letra in cadena:
        if letra == cadena[i]:
            contador += 1
    if contador > 1:
        nueva_cadena += cadena[i]
    contador = 0   

print(nueva_cadena) 