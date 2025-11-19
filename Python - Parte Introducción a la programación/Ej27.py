hubo_diez = False
nota = float(input("Introduce una nota (0-10) o -1 para terminar: "))
while nota != -1:
    if nota == 10:
        hubo_diez = True
    nota = float(input("Introduce una nota (0-10) o -1 para terminar: "))

if hubo_diez:
    print("Sí, se introdujo al menos un 10.")
else:
    print("No se introdujo ningún 10.")
