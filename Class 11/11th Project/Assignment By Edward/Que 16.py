import math
for k in range(2,1000):
    for j in range(2,k):
        if k%j==0:
            break         
    else:
        n=k
        c=0
        a=n
        b=n
        while 1:
            n=math.floor(n/10)
            c=c+1
            if(n==0):
                break
        f=0
        d=c
        i=1
        while i<=c:
            e=a%10
            f=f+e*(10**(d-1))
            a=math.floor(a/10)
            d=d-1
            i=i+1
            if d==0:
                break
        if f==b:
            print("Palindrome Prime :-", f)
    
