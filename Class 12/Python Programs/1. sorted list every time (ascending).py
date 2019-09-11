def insertion_sort(n):
    l=[]
    r=1
    while (r<=n):
        r=r+1
        v=int(input("Enter The Element :- "))
        l.append(v)
        for i in range  (1,len(l)):
            c=l[i]
            k=i-1
            while (k>=0) and (c<=l[k]) :
                l[k+1] = l[k]
                k=k-1
            l[k+1] = c
        print(l)

n=int(input("Enter No. Of Elements in List :- "))
s=insertion_sort(n)

    
