'''Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
Visualizar el descuento y el total a pagar por la compra.'''

monto = int(input("Introduzca el monto de su compra "))
dia = input(
    "Introduzca el día de la semana que hizo su compra (Lunes - Viernes) ").lower()
descuento = 0
if (dia == 'martes' or dia == 'jueves'):
    descuento = 0.15 * monto
    total = monto - descuento
    print(
        f"Se descuenta un {descuento} euros de su compra. El total a pagar es: {total} euros")
else:
    print(f"No tiene ningún descuento. El total a pagar es: {monto} euros")
