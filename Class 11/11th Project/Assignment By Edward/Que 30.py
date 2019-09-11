# To print the upper triangle matrix
print("This programme prints the upper triangle matrix of a square matrix : ")
n=int(input("Enter the number of elements in one side of the matrix : "))
x=[[i for i in range(0,n)] for j in range(0,n)]
print("Enter ",(n**2)," elements in the ",n,"x",n," matrix : ")
for i in  range(0,n):
    for j in range(0,n):
        x[i][j]=int(input())
print("Your matrix is : ")
for i in range(0,n):
    for j in range(0,n):
        print(x[i][j],end="\t")
    print()
print("The upper right triangle of the matrix is : ")
for i in range(0,n):
    for j in range(0,n):
        if i<=j:
            print(x[i][j],end="\t")
        else:
            print(" ",end="\t")
    print()
print("The lower left  triangle of the matrix is : ")
for i in range(0,n):
    for j in range(0,n):
        if i>=j:
            print(x[i][j],end="\t")
        else:
            print(" ",end="\t")
    print()
    
