'''Verificar si un carácter específico está en la cadena con un ciclo y comparaciones.'''

lista = set()

cadena = input("Introduzca una cadena de caracteres ")

for i in range(len(cadena)):
    
    if cadena[i] == "a" or cadena[i] == "A":
        lista.add(cadena[i])
    elif cadena[i] == "p" or cadena[i] == "P":
        lista.add(cadena[i])
    elif cadena[i] == "j" or cadena[i] == "J":
        lista.add(cadena[i])

print(f"Los caracteres que concuerdan son: {lista}")
    