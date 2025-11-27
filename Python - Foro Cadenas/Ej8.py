'''Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower()).'''

palabra_mayus = ""
palabra_minus = ""
valor_letra = 0
palabra = input("Introduzca una palabra ")

eleccion = int(input("Introduzca un el número de una de estas opciones: \n1 - Convertir palabra a MAYÚSCULAS \n2 - Convertir palabra a minúsculas \n"))

match(eleccion):
    case 1:
        for letra in palabra:
            if ord(letra) >= 97 and ord(letra) <= 122:
                valor_letra = ord(letra) - 32
                palabra_mayus += chr(valor_letra)
            else:
                palabra_mayus += letra      
        print(f"Su palabra en MAYÚSCULAS es: {palabra_mayus}")   
    case 2:
        for letra in palabra:
            if ord(letra) <= 90 and ord(letra) >=32 :
                valor_letra = ord(letra) + 32
                palabra_minus += chr(valor_letra)
            else:
                palabra_minus += letra 
        print(f"Su palabra en minúsculas es: {palabra_minus}") 
    case _:
        print("ERROR. Fallo de selección numérica.")