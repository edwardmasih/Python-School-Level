# Checks if the entered number is Armstrong.

import math
n=int(input("Enter the number - "))
b=n
c=0
while 1:
    a=n%10
    c=c+a**3
    n=math.floor(n/10)
    if n==0:
        break
if b==c:
    print("The number is Armstrong")
else:
        print("The number is not Amstrong")
    
    
