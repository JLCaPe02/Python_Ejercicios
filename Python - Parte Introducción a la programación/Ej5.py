import math
radio = float(input("Introduce el radio: "))
diametro = radio * 2
longitud_circunferencia = math.pi * diametro
area_circulo = math.pi * (radio ** 2)
volumen_esfera = (4/3) * math.pi * (radio ** 3)
print(f"Longitud de la circunferencia: {longitud_circunferencia}")
print(f"Área del círculo: {area_circulo}")
print(f"Volumen de la esfera: {volumen_esfera}")
