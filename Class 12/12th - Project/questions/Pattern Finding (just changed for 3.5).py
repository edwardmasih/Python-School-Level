import random
print ("Program -  Pattern Finding ")
print ()
print ("This Program Is Created By Edward Masih & Pranjal Sahu ")
print ("Of Class 12th Batch 2014-15")
print ()


x=[[i for i in range(10)]for j in range(10)]
for i in range(10):
    for j in range(10):
        x[i][j]=random.randint(0,1)
#________________________________________________________________________________

for i in range(10):
    for j in range(10):
        print (x[i][j],' | ')
    print()
print()
#_______________________________________________________________________________

a=int(input("Enter the number of rows :-"))
t=int(input("Enter the number of columns :-"))
print ("Enter the elements according to given positions")
print ()
      
c=1
u=[[m for m in range(a*t)] for n in range(a*t)]
for m in range(a):
    for n in range(t):
        u[m][n]=c
        c=c+1

for m in range(a):
    for n in range(t):
        print (u[m][n],' | ')
    print()
print()

#_______________________________________________________________________________
d=1
y=[[k for k in range(a*t)] for l in range(a*t)]
for k in range(a):
   for l in range(t):
       print (d,"-")
       y[k][l]=int(input())
       d=d+1
print()

#_______________________________________________________________________________

print("your pattern is:")
for i in range(a):
    for j in range(t):
        print (y[i][j]," | ")
    print()
print()
#______________________________________________________________________________
         
l=[[i for i in range((10-a+1)*(10-t+1))]for j in range((10-a+1)*(10-t+1))]
for i in range(10-a+1):
    for j in range(10-t+1):
        l[i][j]=[[k for k in range(a*t)]for m in range(a*t)]
        for m in range(a):
            for n in range(t):
                l[i][j][m][n]=x[i+m][j+n]

#_____________________________________________________________________________
e=0
q=[]
for i in range(10-a+1):
    for j in range(10-t+1):
        for m in range(a):
            for n in range(t):
                if l[i][j][m][n]==y[m][n]:
                    e=e+1
        q.append(e)
        e=0

b=[]

for i in range(len(q)):
    if q[i]==a*t:
        b.append(i)



#______________________________________________________________________________
C=-1
L=[[i for i in range((10-a+1)*(10-t+1))]for j in range((10-a+1)*(10-t+1))]
for i in range(10-a+1):
    for j in range(10-t+1):
        C=C+1
        L[i][j]=C

D=[]
for k in range(len(b)):
    for i in range(10-a+1):
        for j in range(10-t+1):
            if L[i][j]==b[k]:
                D.append(i)
                D.append(j)
#_______________________________________________________________________________


for m in range(0,len(D),2):
    for i in range(a):
        for j in range(t):
            o=D[m]
            p=D[m+1]
            x[o+i][p+j]="*"
            


if len(b)>0:
    print ("Pattern found",len(b),'times.')
    for i in range(10):
        for j in range(10):
            print (x[i][j],'  |  ')
        print ()

else:
    print ('pattern not found')
