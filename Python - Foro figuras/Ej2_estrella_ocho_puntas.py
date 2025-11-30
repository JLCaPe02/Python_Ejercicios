'''Imprime una estrella de ocho puntas combinando líneas verticales, horizontales y diagonales con asteriscos en una matriz de tamaño impar n x n (ej. 9x9).'''

n = int(input("Introduzca n para el tamaño de la matriz"))
centro  = n//2
print(centro)
for i in range(1, n - 1):
    if i >=1 and i<centro:
        diagonales1 = " " *(i) +"*" + " " * (centro - i) + "*" + " " *(centro - i) + "*"
        print(diagonales1)
    elif(i ==centro):
        print( " " + "*" * n )
    else:
        diagonales2 = " " *(n - i - 1) + "*" + " " * (i - centro) + "*" + " " *(i - centro) + "*"
        print(diagonales2)
        




'''centro = (n//2)
for i in range(0, n):
    for j in range(0, n):
        if (j == centro or i==centro or j == i or j + i == n - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()     '''   

