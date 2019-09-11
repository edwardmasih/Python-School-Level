p=[]
n=int(input("Enter No. Of Points : "))
print
print "Enter The values of X and Y (coordinates) for",n,"different points "
print
for i in range (n):
    x=int(input("Enter Value OF x :- "))
    y=int(input("Enter Value OF y :- "))
    print
    p.append([x,y])
print
print "Given ",n," Coordinates Are :-"
print p

import math
def getDistance(x1,y1,x2,y2):
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

d=[]
for i in range (len(p)):
    for j in range(i+1,len(p)):
        distance = (getDistance (p[i][0],p[i][1],p[j][0],p[j][1]))
        d.append((round(distance,2)))

print d
m=min(d)
print "Min Distance: ",m
for i in range (len(p)):
    for j in range(i+1,len(p)):
        distance = (getDistance (p[i][0],p[i][1],p[j][0],p[j][1]))
        a=(round(distance,2))
        if m==a :
            print "The Shortest Distance Pair Is :- ",[p[i][0],p[i][1]],"&",[p[j][0],p[j][1]]
            

        



        
        
        
    
