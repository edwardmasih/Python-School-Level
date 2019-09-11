print("Enter information for 1st distance :-")
f1=int(input("Enter Feet :- "))
i1=int(input("Enter Inches :- "))
while(i1>=12):
    i1=i1-12
    f1=f1+1
    x=f1
    y=i1
print("First Distance is ",x," Feet & ",y," Inches")
print()

print("Enter infromation for 2nd distance :- ")
f2=int(input("Enter Feet :- "))
i2=int(input("Enter Inches :- "))
while(i2>=12):
    i2=i2-12
    f2=f2+1
    xx=f2
    yy=i2
print("Second Distance is ",xx," Feet & ",yy," Inches")
print()

a=x+xx
b=y+yy
while (b>=12):
    a=a+1
    b=b-12
print("Addition Of Two Distance :- ")
print("Total Distance => ",a,"ft ",b,"inches")
      

