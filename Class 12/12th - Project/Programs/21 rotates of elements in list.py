n=int(input("Enter No. Of terms :- "))           
l=[i for i in range (n)]
for i in range (n):
    l[i]=int(input())
print "Original List: ",l
s=len(l)
last=l[-1]
l.pop(-1)
l.insert(0,last)
print "Rotated List: ",l
