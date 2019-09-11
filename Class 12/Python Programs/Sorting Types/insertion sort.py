def insertion_sort(a):
    for i in range  (1,len(a)):
        c=a[i]
        k=i-1
        while (k>=0) and (c<=a[k]) :
            a[k+1] = a[k]
            k=k-1
        a[k+1] = c

n=int(input("Enter No. Of Elements in List :-s "))
a=[i for i in range (n)]
print ("Enter the Elements one after the other :- ")
for i in range (n):
    a[i]=int(input())
insertion_sort(a)
print(a)
    



