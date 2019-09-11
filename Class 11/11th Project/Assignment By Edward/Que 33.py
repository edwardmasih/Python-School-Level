# To input any matrix and print both the diagonals
print("This programme is to print the diagonals of a square matrix : ")
n=int(input("Enter the number of element of the matrix : "))
x=[[i for i in range(0,n)] for j in range(0,n)]
print("Enter ",(n**2)," elements in the ",n,"x",n," matrix : ")
for i in range(n):
    for j in range(n):
        x[i][j]=int(input())
print("Your matrix is : ")
for i in range(n):
    for j in range(n):
        print(x[i][j],end=" ")
    print()
print("The values on left top diagonal is : ")
for i in range(n):
    print(x[i][i],end="  ")
print()
print("The values on right top diagonal is : ")
for i in range(n):
    print(x[i][n-i-1],end="  ")
