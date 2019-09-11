import math
n=int(input('Enter a Number :- ' ))
i=n
while i>0:
    a=math.sqrt(i)
    b=math.floor(a)
    if a%b==0:
        print(i)
    i=i-1
