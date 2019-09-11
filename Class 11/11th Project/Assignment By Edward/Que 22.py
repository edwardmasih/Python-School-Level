n=31
for i in range (2,n+1):
    x=1
    for j in range (2,i):
        if i%j==0:
            x=0
            break
    if x==1:
        print(i,(2**i)-1)

        
        
