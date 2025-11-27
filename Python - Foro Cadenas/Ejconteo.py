'''Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.'''

cadena = input("Introduzca una cadena de caracteres ")
x = input("Introduzca el caracter que quiere contar: ")
cont = 0
for i in range(len(cadena)):
    if cadena[i] == x:
        cont += 1
        
print(f"El carácter {x} se ha repetido {cont}")   