'''Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de
10.'''

num = int(input("Introduzca un número "))

if num % 10 == 0:
    print(f"El {num} es múltiplo de 10")
else:
    print(f"El {num} no es múltiplo de 10")
