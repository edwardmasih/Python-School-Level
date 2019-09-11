a=int(input("enter coefficient of x square "))
b=int(input("enter coefficient of x "))
c=int(input("enter constant value "))
r1=-b+(b**2-4*a*c)**1/2
if((in r1,(b**2-4*a*c)<0):
    print("The Root is Imaginary")
else:
    print("The Root is Real")
    
r2=-b-(b**2-4*a*c)**1/2
if((in r2,(b**2-4*a*c)<0):
    print("The Root is Imaginary")
else:
    print("The Root is Real")

print("1st Root is ",r1)
print("2nd Root is ",r2)

