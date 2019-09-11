import math
x=int(input("enter the no. "))
n=int(input("enter terms "))

for i in range (1,n+1):
    c=(x**i)/math.factorial(i)
    print(c)
