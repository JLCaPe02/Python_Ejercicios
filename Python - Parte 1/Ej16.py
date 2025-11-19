# Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene.
contador = 0
num = int(input("Introduzca un numero entre 0 y 99999 "))
while num <= 0 or num > 99999:
    num = int(input("Introduzca un numero entre 0 y 99999 "))

num_str = str(num)
for i in range(len(num_str)):
    contador += 1

print(f"Tú número está compuesto por", contador, "cifras")
