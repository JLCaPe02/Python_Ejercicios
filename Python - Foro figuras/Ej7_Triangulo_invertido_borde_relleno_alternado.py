'''Imprime un triángulo invertido de altura n con asteriscos en el borde, y líneas internas de relleno alternadas entre espacios y asteriscos.

Figura para n=6:'''

n = int(input("Introduzca la altura para el triángulo invertido con borde y relleno alternado "))

for i in range(1, n + 1):
    for j in range(1, n + 2):
        if (i == 1 and j<=n) or (i==n and j<=n):
            print("*", end="")
        elif ((i>=2 and i<=n-1) and (i%2==0 and j%2!=0) or j==1 ):
            print("*", end="")
        elif ((i>=2 and i<=n-1) and (i%2!=0 and j==n + 1)):
            print("*", end=" ")
        else:
            print(" ", end="")
    print()


        