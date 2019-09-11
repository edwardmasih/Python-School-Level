import math
d=int(input("Enter the range (>100)- "))
for i in range (2,d):
    v=i
    c=0
    while 1:
        a=v%10
        c=c+a**3
        v=math.floor(v/10)
        if v==0:
            break
    if i==c:
        print("The Armstrong number is",c)
    
 
