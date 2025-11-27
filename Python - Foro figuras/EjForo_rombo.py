'''Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, 
donde solo se imprimen los bordes y el centro.'''

n = int(input("Introduzca un número mayor a cero que servirá como dato para la altura del rombo "))
altura = 2*n -1
print(" " * (n), end="")
print("*")
for i in range(1, n):
    print(" " * (n - i), end="")
    print("*", end="")
    print(" " * ((i*2) - 1), end="" )
    print("*")
    
for j in range(n, 2, -1):
    print(" " * ((n - j )+ 2), end="")
    print("*", end="")
    print(" " * ((j*2) - 5) , end="" )
    print("*") 
print(" " * (n), end="")
print("*") 


for i in range(1, altura - 1):
    if i < n:
        print(" " * (n - i), end="")
        print("*", end="")
        print(" " * ((i*2) - 1), end="" )
        print("*")
    else:
        print(" " * ((i - n) + 2), end="")
        print("*", end="")
        print(" " * (2*(altura - i -1) - 1), end="" )
        print("*")
print(" " * (n), end="")
print("*")
    
    