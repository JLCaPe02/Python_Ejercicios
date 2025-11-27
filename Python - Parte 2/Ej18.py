'''Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia
(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla.'''

A = int(input("Introduzca el número que actuará de base "))
B = int(input("Introduzca el número que actuará de exponente para la base "))
potencia = 1
for i in range(1, B + 1):
    potencia = potencia * A
    
print(f"El valor de la base {A} elevado a la potencia de {B} es: {potencia}")
    