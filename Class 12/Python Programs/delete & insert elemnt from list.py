n=int(input("Enter No. Of terms :- "))           
l=[i for i in range (n)]
for i in range (n):
    l[i]=int(input())
#delete
m=int(input("Enter Element TO Delete "))
if m in l :
    i=l.index(m)
    l.pop(i)
    print(l)
else :
    print ("The No. you gave is not in list")

#insert
q=int(input("Enter Element TO Insert "))
xx=int(input("Enter The index at which you wanna insert the no."))
l.insert(xx,q)
print(l)
