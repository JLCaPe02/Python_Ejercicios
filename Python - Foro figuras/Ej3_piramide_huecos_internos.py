'''Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.'''
'''int(input("Introduzca altura de la pirámide "))'''
n =6
centro = n//2
for i in range(1, n + 1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i - 1):
        if i == centro +1 or i == n or i==1:
            print("*", end="")
        elif k ==0 or k==2*i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

