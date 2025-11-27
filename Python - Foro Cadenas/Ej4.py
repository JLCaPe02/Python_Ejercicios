'''Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas).'''
cadena_invertida= ""
cadena = input("Introduzca cualquier palabra ")



for i in range(len(cadena)):
    cadena_invertida = cadena[i] + cadena_invertida

print(f"Su nueva cadena de caracteres es {cadena_invertida}")