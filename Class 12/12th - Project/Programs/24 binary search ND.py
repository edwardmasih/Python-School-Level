def binary_search(l,m):
    beg=0
    end=len(l)-1
    while beg<=end:
        mid=int((beg+end)/2)
        if l[mid]==m:
            print "Found at", mid+1
            break
        else:
            if l[mid]<m:
                beg=mid+1
            else:
                end=mid-1
            print "Not Found"

n=int(input("Enter No. Of terms :- "))           
l=[i for i in range (n)]
for i in range (n):
    l[i]=int(input())
print l
m=int(input("Enter Element TO Find  "))
a=binary_search(l, m)
print a
