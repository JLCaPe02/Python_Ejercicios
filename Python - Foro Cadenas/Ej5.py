'''Verificar si un carácter específico está en la cadena con un ciclo y comparaciones.'''

lista = set()

cadena = input("Introduzca una cadena de caracteres ").lower()

for i in range(len(cadena)):
    
    if cadena[i] == "a":
        lista.add(cadena[i])
    elif cadena[i] == "p":
        lista.add(cadena[i])
    elif cadena[i] == "j":
        lista.add(cadena[i])

print(f"Los caracteres que concuerdan son: {lista}")
    