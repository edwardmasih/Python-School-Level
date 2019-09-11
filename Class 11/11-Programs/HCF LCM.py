n=int(input("Enter the first Number "))
m=int(input("Enter the second Number "))
#LCM
print()
for i in range (n,(n*m)+1,1):
    if i%n==0 and i%m==0:
        print ("The LCM of the Two Numbers is :-",i)
        break
print()
#HCF
for i in range (n,0,-1):
    if n%i==0 and m%i==0:
        print("The HCF of the Two Numbers is :-",i)
        break
