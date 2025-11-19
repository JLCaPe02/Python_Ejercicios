'''Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre
el porcentaje de descuento realizado'''

p_art = float(input("Introduzca el precio del articulo"))
p_venta = float(input("Introduzca el precio de venta (con descuento)"))

descuento = int(((p_art - p_venta)/p_art) * 100)

print("El descuento aplicado al producto es",
      descuento, "porciento de descuento")
