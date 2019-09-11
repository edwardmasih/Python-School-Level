def locatelargest(a):
    l=[]
    for i in range(n):
        for j in range (x):
            l.append(a[i][j])
    m=max(l)
    print "Largest No. :- ",m
    for i in range (n):
        for j in range (x):
            if a[i][j]==m:
                print "Largest Number Found! "
                print "at row",i+1,"&","column",j+1


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
        print ha[i][j],'\t',
    print

locatelargest(a)
