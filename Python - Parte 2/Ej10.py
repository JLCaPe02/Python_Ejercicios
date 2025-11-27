'''Programa que calcula y escribe la suma y el producto de los 10 primeros números naturales.'''
suma = 0
prod = 1
for i in range(1, 11):
    suma = suma + i
    prod = prod * i
    print(prod)

print(f"La suma de los 10 primeros números naturales es {suma}")
print(f"El producto de los 10 primeros números naturales es {prod}")