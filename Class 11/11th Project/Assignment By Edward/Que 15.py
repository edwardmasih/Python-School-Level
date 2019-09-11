# Que 15

#Pattern A
print("Pattern A is :- ")
print ()
x=6
for i in range (1,x+1):
    for j in range (1,i+1):
        print (i,end="")
    print()
print ()

#Pattern B
print ("Pattern B is :- ")
print ()
while x>=0:
    for k in range (1,x+1):
        print (k,end="")
    print()
    x=x-1
print ()

#Pattern C
print ("Pattern C is :- ")
print()
n=8
for i in range (1,n+1,1):
    for j in range (n-1,0,-1):
        print (" ",end="\t")
    n=n-1
    for k in range (0,i,1):
        print ((2**k),end="\t")
    for l in range (i,1,-1):
        print ((2**(l-2)),end="\t")
    print()
   
