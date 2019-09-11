# Row Wise Matrix Print


row=eval(input("Enter No. Of Rows:- "))
col=eval(input("Enter No. Of Columns:- "))
    
def row_matrix():
    Matrix=[]
    a=row
    b=col
    for r in range(a):
        Matrix.append([])

    for r in range(a):
        for c in range(b):
            value=eval(input("Enter Value Row Wise :- "))
            Matrix[r].append(value)
    print (Matrix)

print()
print(row_matrix())
print("Your Matrix is :- ")
for r in range(row):
    for c in range(col):
        print(m[r][c],end="\t")
    print()

print("The Transpose of matrix is :-")
for r in range(col):
    for c in range(row):
        print(m[c][r],end="\t")
    print()

print(row_matrix())


