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

print "The Rows Are -"
b=[]
for k in range (n):
    b.append([])
for i in range (n):
    for j in range (x):
        b[i].append(a[i][j])
print b
print
s=[]
for k in range (n):
    s.append([])
for i in range (len(b)):
    s[i]=sum(b[i])
print "Sum Of Each Row Elements: ", s
print

print "The Columns Are -"
c=[]
for k in range (x):
    c.append([])
for i in range (x):
    for j in range (n):
        c[i].append(a[j][i])
print c
print

for i in range (len(c)):
    c[i]=sum(c[i])
print "Sum OF Each Column Elements: ",c


        
