import math
a=int(input("Enter coordinate x1 in degrees:- "))
b=int(input("Enter coordinate x2 in degrees:- "))
c=int(input("Enter coordinate y1 in degrees:- "))
d=int(input("Enter coordinate y2 in degrees:- "))

r=6371.01
x1=(math.radians(a))
x2=(math.radians(b))
y1=(math.radians(c))
y2=(math.radians(d))
d=r*(math.cos((math.sin(x1))*(math.sin(x2)))+((math.cos(x1))*(math.cos(x2))*(math.cos(y1-y2))))
print ("Great Cirle Distance is :-",d)
