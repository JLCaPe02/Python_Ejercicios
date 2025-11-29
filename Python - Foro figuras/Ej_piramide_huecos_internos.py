'''Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.'''

n = int(input("Introduzca altura de la pirámide "))

for l in range(1, n + 1):
    print(" " * (n - l), end="")
    if (l == n//2):
        print("*", end="")
        print(" " * (n - l), end="")
        print("*")
    else:
        print("*" * ((l*2) - 1))
    


'''fila_medio=(n//2)+1
for i in range(1, n + 1):
    for j in range(1, n-i+1):
        print(" ", end="")
    ancho_linea=(i*2)-1
    for l in range(1, ancho_linea+1):
        if (i==n or l==1 or l==ancho_linea or (i==fila_medio and l%2!=0)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''