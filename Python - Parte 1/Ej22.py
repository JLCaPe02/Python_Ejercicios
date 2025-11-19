'''Escriba un programa que recibe como datos de entrada una hora expresada en horas,
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
transcurrido un segundo'''

hora = int(input("Introduzca la hora (24h) "))
min = int(input("Introduzca los minutos (60min) "))
seg = int(input("Introduzca los segundos (60seg) "))

while (hora > 24 or hora < 0):
    hora = int(print("Introduzca la hora (24h) "))

while (min > 60 or min < 0):
    min = int(input("Introduzca los minutos (60min) "))

while (seg > 60 or seg < 0):
    seg = int(input("Introduzca los segundos (60seg) "))

seg += 1

if (seg == 60):
    min += 1
    seg = 00
elif (seg == 61):
    min = min + 1
    seg = 1

if (min == 60):
    hora += 1
    min = 0
elif (min == 61):
    hora += 1
    min = 1
elif (min == 62):
    hora += 1
    min = 2

if (hora == 24):
    hora = 0
elif (hora == 25):
    hora = 1


print(f"La hora es {hora}:{min}:{seg}")
