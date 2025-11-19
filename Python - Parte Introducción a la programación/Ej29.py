print("Piensa un número del 1 al 100 y yo intentaré adivinarlo.")
print("Respóndeme 'mayor', 'menor' o 'igual'.")
minimo = 1
maximo = 100
adivinado = False

while not adivinado:
    intento = (minimo + maximo) // 2
    print(f"¿Es tu número {intento}?")
    respuesta = input("Respuesta (mayor/menor/igual): ").lower()

    if respuesta == "igual":
        print("¡Genial! He adivinado tu número.")
        adivinado = True
    elif respuesta == "mayor":
        minimo = intento + 1
    elif respuesta == "menor":
        maximo = intento - 1
    else:
        print("Por favor, responde 'mayor', 'menor' o 'igual'.")

    if minimo > maximo:
        print("¡Algo ha ido mal! Parece que me has mentido.")
        break
