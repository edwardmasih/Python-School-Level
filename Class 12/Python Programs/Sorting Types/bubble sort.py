def bubble_sort(b):
    v=len(b)
    for i in range(v):
        for j in range((v-1)-i):
            if b[j] >b[j+1]:
                temp = b[j+1]
                b[j+1] = b[j]
                b[j] = temp
            print (b)
        print (b)
b=[7,4,1,2,30,0]

bubble_sort(b)


