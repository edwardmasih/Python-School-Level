def matrix(n,x):
    a=[[i for i in range (n*x)] for j in range (n*x)]
    print("Enter Values One By One ;- ")
    for i in range (n):
        for j in range (x):
            a[i][j]=int(input())
    print()
    print("Your Matrix is - ")
    for i in range (n):
        for j in range (x):
            print(a[i][j],end="\t")
        print()

    print()
    print("The Rows Are -")
    b=[]
    for i in range (n):
        b.append([])
    for i in range (n):
        for j in range (x):
            b[i].append(a[i][j])
    print(b)

    print()
    print("Transpose of Your Matrix is -")
    for i in range (x):
        for j in range (n):
            print(a[j][i],end="\t")
        print()

    print()
    if n==x:
        print("First Diagonal ;- ")
        for i in range (n):
            for j in range (x):
                if i==j:
                    print(a[i][i],end="\t")
        print()

        print("second Diagonal ;- ")
        for i in range (n):
            for j in range (x):
                if i+j==n-1:
                    print(a[i][j],end="\t")
    else:
        print("Diagonals Not Possible (Sorry)")
    # triangles
    print()
    print()
    
    if n==x:
        print("The Lower Triangle is :- ")
        for i in range (n):
            for j in range (i+1):
                print(a[i][j],end="\t")
            print()
        print()
        print("The Upper Triangle is :- ")
        for i in range (n):
            for k in range (i):
                print("",end="\t")
            for j in range (i,x):
                print(a[i][j],end="\t")
            print()
        print()
    else:
        print("Triangles Not Possible (Sorry)")

n=int(input("Enter rows for 1st matrix:- "))
x=int(input("Enter columns for 1st matrix:- "))
m=matrix(n,x)

                


               
