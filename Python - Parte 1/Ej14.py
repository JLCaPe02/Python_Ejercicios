# Escriba un programa que lea dos números y nos diga cual es mayor o si son iguales

num1 = int(input("Introduce número uno "))
num2 = int(input("Introduce número dos "))

if num1 > num2:
    print(f"El numero {num1} es mayor y numero {num2} es menor")
elif num2 > num1:
    print(f"El numero {num2} es mayor y numero {num1} es menor")
else:
    print(f"El numero {num1} y numero {num2} son iguales")
