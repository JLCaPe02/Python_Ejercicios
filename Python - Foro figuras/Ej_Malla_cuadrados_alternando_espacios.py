n = int(input("Introduzca la altura para el cudrado ")) 

lado = 2*n + 1

for i in range(1, lado + 1):
    for j in range(1, lado + 1):
        if(i==1 or i == lado or j ==1 or j == lado or i%2!=0 or j%2!=0):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()