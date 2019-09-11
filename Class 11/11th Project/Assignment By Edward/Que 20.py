# Que 20  Leap Year

print ("Leap Year Has 366 Days...")
print ('The Year Perfectly Divisible by 4 is A Leap Year')
z=0
for i in range(2010,2101,1):
    if i%4==0:
        z=z+1
        if z<=10:
            print(i,end=" ")
        else:
            z=1
            print()
            print(i,end=" ")
