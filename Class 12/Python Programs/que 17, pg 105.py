def bubble_sort(b):
    i = 0
    j = 0
    v=len(b)
    for i in range(v):
        for j in range((v+1)-i):
            if b[j] > b[j+1]:
                temp = b[j+1]
                b[j+1] = b[j]
                b[j] = temp
    print (b)

c="Enter Item Code :- ","Enter Item Name :- ","Enter Quantity :- ","Enter Price :-"
n=int(input("Enter No. Of Products :- "))
b=[i for i in range (n)]
for i in range (n):
    for j in range (0,4):
        b[i]=input(c[j])
bubble_sort(b)
print("Sorted :- ",b)

