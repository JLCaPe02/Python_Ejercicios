cantidad = int(input("Introduce una cantidad de euros (múltiplo de 5): "))

if cantidad % 5 != 0:
    print("La cantidad debe ser múltiplo de 5.")
else:
    billetes = [500, 200, 100, 50, 20, 10, 5]
    print("Para alcanzar {cantidad}€ necesitas:")

    for billete in billetes:
        numero_billetes = cantidad // billete
        if numero_billetes > 0:
            print(f"{numero_billetes} billete(s) de {billete}€")
            cantidad = cantidad % billete
