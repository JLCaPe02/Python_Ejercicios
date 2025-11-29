'''Imprime un cuadrado de lado n con bordes de asteriscos y las dos diagonales marcadas, dejando espacios en el resto.
Figura para n=7:'''

n = int(input("Introduzca altura de la pirámide "))
mitad = (n*2)//2
mitad_n = n//2
for i in range(1, n*2):
    for j in range(1, n + 1):
        if (i == n*2 -1 or i==1) or ((j==1 or j==n)) and i%2!=0:
            print("*", end="")
        elif((i%2!=0 and (i== 3 or i==n*2-3) and j==3) or ((j >=4 and j<n-2) and (i == mitad - 2 or i == mitad + 2)) or (i==mitad and j== n-2 and i%2!=0)):
             print("*", end="")
        else:
            print(" ", end="")
    print()
