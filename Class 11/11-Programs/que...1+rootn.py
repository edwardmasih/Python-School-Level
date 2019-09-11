import math
n=int(input("Enter the terms "))
for i in range (1,n+1):
    c=((1/math.sqrt(i))+(math.sqrt(i+1)))
    print(c)
