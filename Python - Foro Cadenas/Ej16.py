'''Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo).'''

cadena1 = input("Introduzca su primera cadena de caracteres ")

cadena2 = input("Introduzca su segunda cadena de caracteres ")

nueva_cadena = ""
for letra in cadena1:
    nueva_cadena+=letra

for letra in cadena2:
    nueva_cadena += letra

print(f"La concatenación de las dos cadenas anteriores es {nueva_cadena}")