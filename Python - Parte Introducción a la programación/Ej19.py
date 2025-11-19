num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

if num1 == num2 and num2 == num3:
    print("Los tres números son iguales")
else:
    mayor = num1
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3

    menor = num1
    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor = num3

    print(f"El mayor es: {mayor}")
    print(f"El menor es: {menor}")

    if num1 == num2:
        print("El primero y el segundo son iguales")
    elif num1 == num3:
        print("El primero y el tercero son iguales")
    elif num2 == num3:
        print("El segundo y el tercero son iguales")
