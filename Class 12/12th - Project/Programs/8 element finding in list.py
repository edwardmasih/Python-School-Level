def search(l, ele):
    size=len(l)
    for i in range (size):
        if ele==l[i]:
            pos=i
            print "found at",pos+1
            break     
    else :
        print "not Found"

    
                          
n=int(input("Enter No. Of terms :- "))           
l=[i for i in range (n)]
for i in range (n):
    l[i]=int(input())
m=int(input("Enter Element TO Find  "))
a=search(l, m)
print a
