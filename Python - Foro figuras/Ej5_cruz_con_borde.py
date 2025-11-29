'''Imprime una cruz en una matriz de tamaño n x n con puntos en el borde, asteriscos en las líneas vertical y horizontal centrales, y espacios en el resto.'''
n = 7
mitad_col = n//2

for i in range(1, n + 1):
    for j in range(1, n+1):
        if i == 1 or i == n or j==1 or j==n:
            print(".", end=" ")
        elif i==mitad_col + 1:
            print("*", end=" ")
        elif (j == mitad_col + 1 and i%2==0) or i == j or i + j == n + 1:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()
