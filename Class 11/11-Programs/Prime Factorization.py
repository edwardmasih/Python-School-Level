n=int(input("Enter a Number ==> "))
print()

print("The Prime Factors of The Number Given By You are:- ")
for i in range (2,n):
    if n%i==0:
        count=0
        while (n%i==0):
            n=n/i
            count=count+1
        print(i,"*",count)

