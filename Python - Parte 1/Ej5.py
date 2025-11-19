'''Escriba un programa que toma como dato de entrada un número que corresponde a la
longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la esfera
que corresponde con dicho radio'''

long_radio = int(input("Introduzca la longitud del radio "))

diametro = long_radio * 2
radio = diametro/2

long_circunferencia = 3.14 * diametro
a_circulo = 3.14 * radio**2
v_esfera = 4/3 * 3.14 * radio**3

print(f"La longitud de la circunferencia es: {long_circunferencia}")
print(f"El area del circulo es: {a_circulo}")
print(f"El volumen de la esfera es: {v_esfera}")
