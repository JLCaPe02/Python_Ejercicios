'''Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero).'''

num1 = int(input("Introduce número uno "))
num2 = int(input("Introduce número dos "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

print(f"La suma de los números es: {suma}")
print(f"La resta de los números es: {resta}")
print(f"La producto de los números es: {producto}")

if (num1 == 0 or num2 == 0):
    print("No se puede realizar la división porque uno de los números es cero")
else:
    division = num1/num2
    print(f"La división de los números es: {division}")
