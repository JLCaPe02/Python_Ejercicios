'''Programa donde el usuario "piensa" un número del 1 al 100 y el ordenador intenta
adivinarlo. Es decir, el ordenador irá proponiendo números una y otra vez hasta adivinarlo (el
usuario deberá indicarle al ordenador si es mayor, menor o igual al número que ha pensado).'''

numAdivinado = 50
flag = 0
respuesta = ""
print("Piensa en un número del 1 al 100")

while flag == 0:
    respuesta = input(f"Su número es mayor, menor o igual a {numAdivinado} ").lower()
    
    match(respuesta):
        case "mayor":
            numAdivinado += 1
        case "menor":
            numAdivinado -= 1
        case _:
            flag += 1
            print("He adivinado su número")

       
    
    
    
