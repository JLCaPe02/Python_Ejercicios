suma_pares = 0
suma_impares = 0
i = 100
while i <= 200:
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
    i += 1
print(f"Suma de pares (100-200): {suma_pares}")
print(f"Suma de impares (100-200): {suma_impares}")
