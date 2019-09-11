k=int(input("Enter Any Number "))
i=2
c=1
while i<k:
    if (k%i==0):
        c=c+1
    i=i+1
if (c==1):
    print("The Number is Prime")
else:
    print("The Number is Not-Prime")
        
