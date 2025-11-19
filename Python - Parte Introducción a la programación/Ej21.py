contador = 0
ha_leido_negativo = False
while contador < 100:
    num = float(input(f"Introduce el número {contador + 1}/100 (no nulo): "))
    if num == 0:
        print("Ha introducido un cero, intente de nuevo.")
        continue
    if num < 0:
        ha_leido_negativo = True
    contador += 1

if ha_leido_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se han leído números negativos.")
