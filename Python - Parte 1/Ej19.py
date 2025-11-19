'''Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
con el siguiente menú de opciones:
Bienvenido a su Cajero Virtual
1. Ingresar dinero en cuenta
2. Retirar dinero de la cuenta
3. Salir'''

saldo = 1000
salir = 0

while salir == 0:
    seleccion = int(input(
        "Introduzca una de las siguientes opciones: \n1. Ingresar dinero en cuenta\n2. Retirar dinero de la cuenta\n3. Salir\n"))
    match (seleccion):
        case 1:
            ingreso = int(input("Introduzca el numero de dinero a ingresar "))
            saldo += ingreso
        case 2:
            retirar = int(input("Introduzca el numero de dinero a retirar "))
            saldo -= retirar
        case _:
            salir = 3

print("Tu saldo es: ", saldo)
