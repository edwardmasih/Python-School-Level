import math
r=int(input("Enter radian "))
theta=int(input("Enter Theta "))
t=math.radians(theta)
x=r*(math.cos(t))
y=r*(math.sin(t))
print("Coordiantes are :- ",(x,y))
