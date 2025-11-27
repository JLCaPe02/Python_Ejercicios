'''Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.'''
cont = 0
cadena = input("Introduzca una cadena de caracteres ")
x = input("Introduzca el caracter que quiere contar: ")

for i in range(len(cadena)):
    if cadena[i] == x:
        cont += 1
        
print(f"El carácter {x} se ha repetido {cont}")   