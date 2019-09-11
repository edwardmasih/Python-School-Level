#Que 10 and 19 -- Change Decimal To Hex
import math
x=int(input("Enter A Decimal :- "))
while 1:
    r=x%16
    x=math.floor(x/16)
    if r==10:
        print("A",end="")
    elif r==11:
        print("B",end="")
    elif r==12:
        print("C",end="")
    elif r==13:
        print("D",end="")
    elif r==14:
        print("E",end="")
    elif r==15:
        print("F",end="")
    else:
        print(r,end="")
    if x==0:
        break
    






