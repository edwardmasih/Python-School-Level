x=float(input("Enter x : "))
y=float(input("Enter y : "))
if(x>200): 
    print("The coordinate (",x,",",y,") is outside the triangle.")
elif(y>100):
    print("The coordinate (",x,",",y,") is outside the triangle.")
elif(0<x<200):
    if(0<y<100):
        print("The coordinate (",x,",",y,") is inside the triangle.")
else:
    print("The coordinate (",x,",",y,") is outside the triangle.")
