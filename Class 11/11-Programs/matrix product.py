
import random
m1=int(input ("Enter total number of rows in the first matrix "))
n1=int(input ("Enter total number of columns in the first matrix "))
a=[[random.random() for row in range(m1)]for col in range(n1)]
print("Enter Elements one by one")
for i in range(m1):
    for j in range(n1):
        a[i][j]=input()
m2=int(input ("Enter total number of rows in the second matrix "))
n2=int(input ("Enter total number of columns in the second matrix "))
b=[[random.random() for row in range(m1)]for col in range(n1)]
print("Enter Elements one by one")
for i in range(m2):
    for j in range(n2):
        b[i][j]=input()
c=[[random.random() for row in range(m1)]for col in range(n2)]
if (n1==m2):
    for i in range(m1):
        for j in range(n2):
            c[i][j]=0
        for k in range(n1):
            c[i][j]+=a[i][k]*b[k][j]
            print("Your matrix with both the above matrix multiplied : ")
            print (c[i][j],'\t')
            print()
else:
    print ("Multiplication not possible")
