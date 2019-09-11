# Find Runway Length

v=float(input("Enter The Velocity of Plane in m/s :- "))
a=float(input("Enter The Acceleration of Plane in meter per Second square :- "))
l=((v**2)/(2*a))
print ("The Minimum Runway Length Required For The plane is ",l," meters")
le=l/1000
print ("The Minimum Runway Length Required For The plane is ",le," kilometers")
