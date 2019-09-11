import math
def binary(n):
    l=[]
    b=1
    while (n>=1):
        c=n%2
        c=math.floor(c)
        l.append(c)
        n=n/2
    a=l[::-1]
    print(a)
n = int(input("Enter an integer: "))
binary(n)
