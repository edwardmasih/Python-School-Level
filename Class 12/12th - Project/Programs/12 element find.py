def search(l, ele):
    size=len(l)
    for i in range (size):
        if ele==l[i]:
            pos=i
            print "found at",pos+1
            break     
    else :
        print "not Found"

def bubble_sort(b):
    v=len(b)
    for i in range(v):
        for j in range((v-1)-i):
            if b[j] >b[j+1]:
                temp = b[j+1]
                b[j+1] = b[j]
                b[j] = temp
            
    print "Sorted List=> ",b
    
n=int(input("Enter No. Of terms :- "))           
l=[i for i in range (n)]
for i in range (n):
    l[i]=int(input())
bubble_sort(l)
m=int(input("Enter Element TO Find  "))
a=search(l, m)
print a
