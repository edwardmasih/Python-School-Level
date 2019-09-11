b=[9,6,3,2,5,8,7,4,1,0]

def selection_sort(b):
    for i in range((len(b))-1):
        min = b[i]
        for j in range(i + 1, len(b)):
            if b[j] < min:
                min = b[j]
                pos=j
                b[pos] = b[i]
                b[i]=min
        print(b)
selection_sort(b)
print()

def cbse_selsort(b):
    for i in range(0,len(b)):
        min=i
        for j in range (i+1,len(b)):
            if b[j] < b[min]:
                min=j
        pos=b[min]
        b[min]=b[i]
        b[i]=pos
        print(b)

b=[9,6,3,2,5,8,7,4,1,0]
cbse_selsort(b)
