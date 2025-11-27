'''Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.'''
contador = 0
cadena = input("Introduzca una cadena de caracteres o palabra ")

for letra in cadena:
    if letra.isdigit() == True:
        contador += 1

print(f"Su cadena/palabra contiene {contador} vocales")