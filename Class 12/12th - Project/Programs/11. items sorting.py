items=[]
b=items
n=int(input("Enter No. Of Items :- "))
print
for i in range (n):
    name=input("Enter Item Name :- ")
    ino=input("Enter Item No. :- ")
    price=input("Enter Price :- ")
    qty=input("Enter Quantity :- ")
    print
    items+=[[name,ino,price,qty]]

print "ORIGINAL LIST :- ",items
#a        
def insertion_sort_qty(items):
    v=len(items)
    for i in range(v):
        c=items[i]
        k=i-1
        while (k>=0) and (items[i][3]>=items[k][3]) :
            items[k+1] = items[k]
            k=k-1
            items[k+1] = c
        print
    print "Descending Order By Quantity (Using Insertion Sort)"
    print "SORTED LIST:- ",items

#b
def bubble_sort_price(b):
    v=len(b)
    for i in range(v):
        for j in range((v-1)-i):
            if b[j][2] < b[j+1][2]:
                temp = b[j+1]
                b[j+1] = b[j]
                b[j] = temp
        
    print "Ascending Order By Price (Using Bubble Sort)"
    print "SORTED LIST:- ",b

    

insertion_sort_qty(items)
print
bubble_sort_price(b)
