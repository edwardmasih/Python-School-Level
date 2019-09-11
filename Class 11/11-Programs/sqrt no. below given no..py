import math
n=int(input('Enter a Number :- ' ))
for i in range (n,n,1):
    for j in range(n,n-1,-1):
        while j**j==i:
            print (i and j)
