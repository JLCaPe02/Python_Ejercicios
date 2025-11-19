num_n = int(
    input("Introduce un número positivo (N) para calcular su factorial: "))
factorial = 1
if num_n < 0:
    print("El número debe ser positivo.")
elif num_n == 0:
    print("El factorial de 0 es 1")
else:
    i = 1
    while i <= num_n:
        factorial = factorial * i
        i += 1
    print(f"El factorial de {num_n} es {factorial}")
