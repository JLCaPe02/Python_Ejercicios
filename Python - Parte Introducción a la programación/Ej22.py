contador = 0
positivos = 0
negativos = 0
while contador < 100:
    num = float(input(f"Introduce el número {contador + 1}/100 (no nulo): "))
    if num == 0:
        print("Ha introducido un cero, intente de nuevo.")
        continue

    if num > 0:
        positivos += 1
    else:
        negativos += 1
    contador += 1

print(f"Total de números positivos: {positivos}")
print(f"Total de números negativos: {negativos}")
