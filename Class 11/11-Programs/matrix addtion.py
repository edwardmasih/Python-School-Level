
print("This programme is to print the sum of a square matrix : ")
n=int(input("Enter the number of element of the matrix : "))
x=[[i for i in range(0,n)] for j in range(0,n)]
print("Enter ",(n**2)," elements in the ",n,"x",n," matrix : ")
for i in range(n):
    for j in range(n):
        x[i][j]=int(input())
print("Your matrix is : ")
for i in range(n):
    for j in range(n):
        print(x[i][j],end="\t")
    print()
print()

b=[[i for i in range(n)] for j in range(n)]
print("Enter the new elements for new matrix of same length")
for i in range (n):
    for j in range(n):
        b[i][j]=int(input())
print("Your New matrix is : ")
for i in range(n):
    for j in range(n):
        print (b[i][j],end="\t")
    print()

print()
print("Your matrix with both the above matrix added : ")
for i in range(n):
    for j in range(n):
        c=(x[i][j])+(b[i][j])
        print (c,end="\t")
    print()
