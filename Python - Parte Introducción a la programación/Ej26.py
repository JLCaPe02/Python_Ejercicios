nombre_trabajador = input("Nombre del trabajador: ")
horas_trabajadas = float(input("Horas trabajadas en la semana: "))
tarifa_normal = float(input("Tarifa por hora normal: "))

if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * tarifa_normal
else:
    horas_normales = 35
    horas_extra = horas_trabajadas - 35
    salario_bruto = (horas_normales * tarifa_normal) + \
        (horas_extra * tarifa_normal * 1.5)

impuestos = 0
if salario_bruto > 500:
    if salario_bruto <= 900:
        impuestos = (salario_bruto - 500) * 0.25
    else:
        impuestos = (400 * 0.25) + (salario_bruto - 900) * 0.45

salario_neto = salario_bruto - impuestos

print(f"\n--- Recibo de Salario ---")
print(f"Trabajador: {nombre_trabajador}")
print(f"Salario Bruto: {salario_bruto:.2f}€")
print(f"Tasas (Impuestos): {impuestos:.2f}€")
print(f"Salario Neto: {salario_neto:.2f}€")
