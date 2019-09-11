def conv(x):
    if x==1:
        return"One"
    if x==2:
        return"Two"
    if x==3:
        return"Three"
    if x==4:
        return"Four"
n=int(input("Enter Number between 1 and 4: "))
print(n," in words is ",conv(n))

