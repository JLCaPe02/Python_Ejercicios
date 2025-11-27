'''Programa que lea un número positivo N y calcule y visualice su factorial N! Siendo el
factorial:
0! = 1
1! = 1
2! = 2 * 1
3! = 3 * 2* 1
N! = N * (N-1) * (N-2) * … * .'''


n = int(input("Introduzca un número positivo "))
while n <= 0:
    n = int(input("Introduzca un número positivo "))
    
factorial = 0
for i in range(0, n + 1):
    if i==0:
        factorial = 1
    elif i == 1:
        factorial = factorial * 1
    else:
        factorial = factorial * (i)

print(factorial)
    