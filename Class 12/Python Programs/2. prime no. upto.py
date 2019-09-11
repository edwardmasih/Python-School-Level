def prime():
    for i in range (2,n+1):
        x=1
        for j in range(2,i):
            if (i%j==0):
                x=0
                break
        if x==1:
            print(i)
n=int(input("Enter The No. of Terms :- "))
print("1")
prime()
