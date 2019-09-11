def digisum(n):
    r=0
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    return (s)
n=int(input("Enter the number : "))
s=digisum(n)
print("The sum of digits of the number ",n," is : ",s)
