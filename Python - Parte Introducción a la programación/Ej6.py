precio_original = float(input("Introduce el precio original: "))
precio_venta = float(input("Introduce el precio de venta real: "))
descuento = precio_original - precio_venta
porcentaje_descuento = (descuento / precio_original) * 100
print(f"El porcentaje de descuento es: {porcentaje_descuento}%")
