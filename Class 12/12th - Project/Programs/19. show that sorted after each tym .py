def insertion_sort(a):
    print "Insertion Sort"
    for i in range  (1,len(a)):
        c=a[i]
        k=i-1
        while (k>=0) and (c<=a[k]) :
            a[k+1] = a[k]
            k=k-1
            a[k+1] = c
        print a

def selection_sort(b):
    print "Selection SOrt"
    for i in range(0,len(b)):
        min=i
        for j in range (i+1,len(b)):
            if b[j] < b[min]:
                min=j
                pos=b[min]
                b[min]=b[i]
                b[i]=pos
    print(b)

        

b=[6,5,4,3,7,1,2]
insertion_sort(b)
print
selection_sort(b)









