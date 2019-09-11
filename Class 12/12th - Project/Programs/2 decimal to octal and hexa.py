# decimal to binary, octal and hexadecimal
import math
print "Decimal To Binary Press 1"
print "Decimal To Octal Press 2"
print "Decimal To Hexadecimal Press 3"
i=int(input("Enter Your Choice :-"))
n=int(input("Enter A Decimal Number :-"))

if i==1:
    def binary(n):
        l=[]
        b=1
        while (n>=1):
            c=n%2
            c=int(math.floor(c))
            l.append(c)
            n=n/2
        a=l[::-1]
        print "Binary Of Given No :-",a
    binary(n)
    
if i==2:
    l=[]
    b=1
    while (n>=1):
        c=n%8
        c=int(math.floor(c))
        if i==8:
            i=10
        if i==9:
            i=11
        if i==10:
            i=12
        if i==11:
            i=13
        if i==12:
            i=14
        if i==13:
            i=15
        if i==14:
            i=16
        if i==15:
            i=17
        l.append(c)
        n=n/8
    a=l[::-1]
    print "Octal Of Given No :-",a
  
    
if i==3:
        l=[]
        b=1
        while (n>=1):
            c=n%16
            c=int(math.floor(c))
            if c==10:
                c='A'
            if c==11:
                c='B'
            if c==12:
                c='C'
            if c==13:
                c='D'
            if c==14:
                c='E'
            if c==15:
                c='F'
            l.append(c)
            n=n/16
        a=l[::-1]
        print "Hexadecimal Of Given No :-",a
    
    #print "Hexadecimal Of Given No:",b
    
