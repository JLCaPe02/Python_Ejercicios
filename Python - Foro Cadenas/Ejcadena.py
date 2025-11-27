'''Leer una cadena desde teclado y mostrarla carácter por carácter usando un ciclo for y el índice.'''

cadena =  input("Introduzca una cadena de caracteres ")

for i in range(0, len(cadena)):
    print(cadena[i])