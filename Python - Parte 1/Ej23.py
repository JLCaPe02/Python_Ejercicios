'''Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
según sea el caso y el total a pagar de la compra.'''

v_compra = int(input("Introduzca el valor de su compra "))

medio = input("Seleccione el método para pagar su compra ").lower()
descuento = 0
incremento = 0
if (medio == 'contado'):
    descuento = 0.05 * v_compra
    c_final = v_compra - descuento
    print(f"Su descuento es {descuento} y el total a pagar es {c_final}")
elif (medio == 'efectivo'):
    incremento = 0.03 * v_compra
    i_final = v_compra + incremento
    print(f"Su incremento es {incremento} y el total a pagar es {i_final}")
else:
    print("La opción seleccionada no es válida")
