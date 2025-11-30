'''Imprime un cuadrado de lado n con borde y diagonales en asteriscos, y un cuadro hueco centrado dentro.'''

n = 9
mitad = n//2
for i in range(1, n + 1):
    for j in range(1, n+1):
        if(i==1 or i==n or j==1 or j==n):
            print("*", end="")
        elif((i>=2 and i<=mitad) and (j == i+1 or j + i == n)):
            print("*", end="")
        elif((i>mitad + 1 and i<= n - 1) and (i == j + 1  or j + i == n + 2 )):
            print("*", end="")
        else:
            print(" ", end="")
        
    print()