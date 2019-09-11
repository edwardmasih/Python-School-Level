# Area OF Regular Polygon
import math

n= float(input("Enter The No. Of Sides :- "))
t= float(input("Enter The Length Of Side :- "))
s=math.radians(180/n)
a=(n*(t**2))/(4*math.tan(s))
print(a,"is the area of polygon having ",n, "sides.")
