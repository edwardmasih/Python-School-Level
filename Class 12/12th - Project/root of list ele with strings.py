#funct that takes a list with element and give the square root of elements
import math
def root(l):
    for i in range (len(l)):
        if l[i].isdigit():
            print "Square root of",l[i],"=",math.sqrt(int(l[i]))
    
    
    
n=int(input('Enter No. Of Elements in List '))
l=[i for i in range (n)]
print "Enter The Elements One By One","  It Can Be Strings Too"
for i in range (n):
    l[i]=raw_input()
print l
root(l)
