#Que 12 Quadratic Equations

a= int(input("Enter The Coefficient of x^2 (x square):- "))
b= int(input("Enter The Coefficient of x :- "))
c= int(input("Enter The Constant Term :- "))
D= ((b**2)-(4*a*c))
r1= ((-b)+D)/2*a
r2= ((-b)-D)/2*a

if D>0:
    print ("The Two Roots Of the Equation are :- ",r1,'and',r2)
if D==0:
    print ("The Equation has two Equal Roots and it is :- ",r1,'and',r2)
if D<0:
    print('The Equation has No Real Roots.')
