n=int(input("Enter No. Of Terms :"))
l=[0]
x=0
y=1
for  i in range(n+1):
    c=x+y
    l.append(c)
    x=y
    y=c
print l

    
