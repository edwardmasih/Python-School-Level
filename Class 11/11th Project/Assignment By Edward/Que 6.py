# Area Of Triangle

x1= float(input("Enter The Coordinate x1 :- "))
y1= float(input("Enter The Coordinate y1 :- "))
x2= float(input("Enter The Coordinate x2 :- "))
y2= float(input("Enter The Coordinate y2 :- "))
x3= float(input("Enter The Coordinate x3 :- "))
y3= float(input("Enter The Coordinate y3 :- "))
s1= ((x2-x1)+(y2-y1))**0.5
s2= ((x3-x2)+(y3-y2))**0.5
s3= ((x3-x1)+(y3-y1))**0.5
s=(s1+s2+s3)/2
area=(s*(s-s1)*(s-s2)*(s-s3))**0.5
print ("Area Of Triangle is :- ",area)
