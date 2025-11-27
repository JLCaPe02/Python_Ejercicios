'''Leer una cadena y contar cuántas vocales contiene.'''

cont_vocales = 0

palabra = input("Introduzca una palabra ")

for letra in palabra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        cont_vocales+=1
        
print(f"El número de vocales de su palabra es {cont_vocales}")
