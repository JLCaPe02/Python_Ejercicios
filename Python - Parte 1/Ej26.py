'''En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
Si los tres dados son seis, mostrar el mensaje “Excelente”
Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
Si un dado se obtiene seis, mostrar el mensaje “Regular”
Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
(Use el control switch).'''

import random

resultados = []
i = 0
while (i < 3):
    i += 1
    dado = random.randint(1, 6)
    resultados.append(dado)

cantidad_de_seis = resultados.count(6)

match cantidad_de_seis:

    case 3:
        print("Excelente")
    case 2:
        print("Muy bien")
    case 1:
        print("Regular")
    case 0:
        print("Pésimo")
