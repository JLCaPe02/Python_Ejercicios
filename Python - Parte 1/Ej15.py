'''Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales
son iguales.'''

# Leer los tres números
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

# Analizar los números
if num1 == num2 == num3:
    print("Los tres números son iguales.")
else:
    mayor = int(max(num1, num2, num3))
    menor = int(min(num1, num2, num3))

    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")

    # Comprobar si hay números iguales entre ellos
    if num1 == num2 and num1 != num3:
        print(f"El primer y el segundo número son iguales: {num1}")
    elif num1 == num3 and num1 != num2:
        print(f"El primer y el tercer número son iguales: {num1}")
    elif num2 == num3 and num2 != num1:
        print(f"El segundo y el tercer número son iguales: {num2}")
    else:
        print("Ningún número es igual a otro.")
