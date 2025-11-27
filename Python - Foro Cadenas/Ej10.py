'''Leer una cadena y contar cuántos caracteres son letras mayúsculas.'''

cont_mayus = 0

palabra = input("Introduzca una palabra ")

for letra in palabra:
    if ord(letra) <=90 and ord(letra) >= 32:
        cont_mayus+= 1

print(f"Su palabra contiene {cont_mayus} mayúsculas")