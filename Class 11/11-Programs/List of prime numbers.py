n=int(input("Enter the number upto which you want the prime numbers => "))
print()
print("The List of Prime Nubmber :- ")

for i in range (1,n):
    x=1
    for j in range (2,i):
        n=i%j
        if n==0:
            x=0
            break
    if x==1:
        print(i)
