t=int(input("Enter the time of the particle upto which you want from 0 to ____ <=(your given time) "))
u=int(input("Enter the Initial Velocity of the particle "))
a=int(input("Enter the Acceleration of the particle "))
s=0
while 0<=t:
    s=(u*t)+((1/2)*(a)*(t)**2)
    t=t-1
    print(s)
    
    
    
 
 
    
