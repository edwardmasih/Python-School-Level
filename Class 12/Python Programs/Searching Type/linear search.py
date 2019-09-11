def linear_search(al, ele):
    size=len(al)
    for i in range (size):
        if ele==al[i]:
            pos=i
            print ("found at",pos+1)
            break     
    else :
        print ("not Found")

    
                          
n=int(input("Enter No. Of terms :- "))           
l=[i for i in range (n)]
for i in range (n):
    l[i]=int(input())
m=int(input("Enter Element TO Find  "))
a=linear_search(l, m)
print(a)
