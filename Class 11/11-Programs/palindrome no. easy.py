n=(input("Enter a Number Or Word (word should be in small letters) :- "))
a=list(n)
b=a[::-1]
print("".join(b))
if n==b:
    print("Palindrome")
else:
    print("Not Palindrome")
