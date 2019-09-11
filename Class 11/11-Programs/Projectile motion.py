import math
u=int(input("Enter The Initial Velocity of The Object to be Projected (in m/s)==> "))
a=int(input("Enter The Angle of Projection (in degrees)==> "))

g=9.8
sin = (math.sin(math.radians(a)))
cos = (math.cos(math.radians(a)))

T =(2*u*sin)/g
H =(u**2)*((sin)**2)/(2*g)
R =(2*(u**2)*(sin)*(cos))/g

print()
print()

print("The Time Taken By the Projectile is ",T)
print()

print("The Height is ",H)
print()

print("The Range of the Projectile is ",R)
                                                


                                                
