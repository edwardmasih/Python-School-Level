n=int(input("Enter the number of terms :- "))
for i in range(1,n+1):
    for j in range (n-1,0,-1):
        print("",end="\t")
    n=n-1
    for k in range(i):
        print((2**k),end="\t")
    for l in range(i,1,-1):
        print((2**(l-2)),end="\t")
    print()
