'''Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos.

Figura para n=4:'''

n = 4
'''int(input("Introduzca n para ser posteriormente usada en el cálculo de la altura del rombo sólido "))'''

altura = 2*n - 1
mitad = (altura//2) + 1
for i in range(1, altura + 1):
    if (i <=mitad):
        for j in range(n-i):
            print(" ", end="")
        for k in range(2*i - 1):
            print("*", end="")
        print()
    if (i > mitad and i <=altura):
        for j in range(i - mitad):
            print(" ", end="")
        for k in range(2* (altura -  i) +1):
            print("*" , end="")
            
            
        print()