n=int(input("Enter no. of Rows :-"))
x=int(input("Enter no. of Columns :-"))
a=[[i for i in range (n*x)] for j in range (n*x)]
print "Enter Values One By One ;- "
for i in range (n):
    for j in range (x):
        a[i][j]=int(input())
print
print "Your Matrix is - "
for i in range (n):
    for j in range (x):
        print a[i][j],'\t',
    print
print

def sumMajorDiagonal(b,n):
        s=0
        for i in range (len(b)):
            s=sum(b)
        print "Sum Of Each Elements Of Major Diagonal : ", s
        print
        
def sumMinorDiagonal(s,n):
        k=0
        for i in range (len(s)):
            k=sum(s)
        print "Sum Of Each Elements Of Secondary Diagonal : ", k
        print
        
if n==x:
        print "First (Major) Diagonal ;- "
        b=[]
        for i in range (n):
            for j in range (x):
                if i==j:
                    b.append(a[i][i])
        print b
        print

        print "Second (Secondary) Diagonal ;- "
        s=[]
        for i in range (n):
            for j in range (x):
                if i+j==n-1:
                    s.append(a[i][j])
        print s                 
else:
    print "Diagonals Not Possible (Sorry)"
    
print
sumMajorDiagonal(b,n)
sumMinorDiagonal(s,n)

    

        
        
        
        
