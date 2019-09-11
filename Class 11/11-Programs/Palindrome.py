n=int(input("Enter a three digit Number :- "))
o=n%10
t=(n//10)%10
h=n//100
if o==h:
    print ("Your number is Palindrome")
else:
    print("Your number is NOT Palindrome")
