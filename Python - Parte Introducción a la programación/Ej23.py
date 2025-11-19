positivos = 0
negativos = 0
ha_leido_negativo = False
num = float(input("Introduce un número (o 0 para terminar): "))

while num != 0:
    if num > 0:
        positivos += 1
    else:
        negativos += 1
        ha_leido_negativo = True
    num_23 = float(input("Introduce un número (o 0 para terminar): "))

if ha_leido_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se han leído números negativos.")

print(f"Total de números positivos: {positivos}")
print(f"Total de números negativos: {negativos}")
