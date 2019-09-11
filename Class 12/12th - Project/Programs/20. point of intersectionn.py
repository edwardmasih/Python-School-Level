# Algorithm Based
def line_intersect(x1,y1,x2,y2,x3,y3,x4,y4):
        m1=(y2-y1)/(x2-x1)
        m2=(y4-y3)/(x4-x3)
        c1=(y1-(m1*x1))
        c2=(y3-(m2*x3))
        if m1-m2==0:
                print "Lines Dont Intersect"
                print "Its A Line Itself"
                return None
        else:
                b=[]
                x=(c2-c1)/(m1-m2)
                y=(m1*x)+c1
                b.append([x,y])        
                print "Point Of Intersection :- ",b
a=[]
x1=int(input("Enter x1 :- "))
y1=int(input("Enter y1 :- "))
x2=int(input("Enter x2 :- "))
y2=int(input("Enter y2 :- "))
a.append([x1,y1])
a.append([x2,y2])
m1=((y2-y1)/(x2-x1))  
print "Line 1:",a
print

b=[]
x3=int(input("Enter x3 :- "))
y3=int(input("Enter y3 :- "))
x4=int(input("Enter x4 :- "))
y4=int(input("Enter y4 :- "))
b.append([x3,y3])
b.append([x4,y4])
m2=(y4-y3)/(x4-x3)
print "Line 2:",b
print
               
print "Equation Of Line 1: Y = ",m1,"X","+",y1-(m1*x1)
print "Equation Of Line 1: Y = ",m2,"X","+",y3-(m2*x3)
line_intersect(x1,y1,x2,y2,x3,y3,x4,y4)
        

        


        
        
