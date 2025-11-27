'''Programa que dada una cantidad de euros que el usuario introduce por teclado (múltiplo de
5 €) mostrará los billetes de cada tipo que serán necesarios para alcanzar dicha cantidad
(utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar el mínimo de billetes posible.
Por ejemplo, si el usuario introduce 145 el programa indicará que será necesario 1 billete de 100
€, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo 29 billetes de 5, que aunque
sume 145 € no es el mínimo número de billetes posible).'''

dinero = int(input("Introduzca una cantidad de dinero múltiplo de 5 "))
cont5 = 0
cont10 = 0
cont20 = 0
cont50 = 0
cont100 = 0
cont200 = 0
cont500 = 0

while dinero%5!=0:
    dinero = int(input("Debe introducir una cantidad de dinero que sea múltiplo de 5 "))

while dinero!=0:
    if (dinero >=500):
        dinero = dinero - 500
        cont500 += 1
    elif (dinero >=200 and dinero < 500):
        dinero = dinero - 200
        cont200 += 1
    elif (dinero >=100 and dinero < 200):
        dinero = dinero - 100
        cont100 += 1
    elif (dinero >=50 and dinero < 100):
        dinero = dinero - 50
        cont50 +=1
    elif (dinero >=20 and dinero < 50):
        dinero = dinero - 20
        cont20 +=1
    elif (dinero >=10 and dinero < 20):
        dinero = dinero - 10
        cont10 +=1
    else:
        dinero = dinero - 5
        cont5 +=1

print(f"Para su cantidad de dinero, son necesarios: \n{cont500} billetes de 500 \n{cont200} billetes de 200 \n{cont100} billetes de 100 \n{cont50} billetes de 50 \n{cont20} billetes de 20 \n{cont10} billetes de 10 \n{cont5} billetes de 5")