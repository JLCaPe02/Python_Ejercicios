n =9

centro = (n//2) + 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i==1 or j==1 or i==n or j==n):
            print("*", end=" ")
        elif(i==j or i + j == n+1):
            print("*", end=" ")
        elif (i>=centro-1 and i <=centro + 1 and j >=centro - 1 and j<=centro + 1 ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()