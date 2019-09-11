# To calculate the sum of a particular series
print("To calculate the sum of (x)-(x^3)/(3!)+(x^5)/(5!)-(x^7)/(7!).......upto n terms : ")
x=int(input("Enter the value of x : "))
n=int(input("Enter the value of number of terms  : " ))
s=0
fact=1
for i in range(1,n+1,1):
    fact=fact*(i*2-1)
    if i%2!=0:
        s=s+(x)**(i*2-1)/fact
    else:
        s=s-(x)**(i*2-1)/fact
    fact=fact*(i*2)
print("The sum of the given series is : ",s)
