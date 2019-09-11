n=int(input("enter the terms :-"))
l=[]
print "enter the numbers :-"
for i in range(n):
    a=int(input())
    l.append(a)
def sort(b):
    for i in range((len(b))-1):
        min = b[i]
        for j in range(i + 1, len(b)):
            if b[j] < min:
                min = b[j]
                pos=j
                b[pos] = b[i]
                b[i]=min
sort(l)                
print l

d="y"
while d=="y":
    print "Want to insert any other number??? y-yes, n-no"
    d=(input())
    if d!="y":
        print "Bye"
        break
    x=int(input "enter the number to enter :-"))
    l.append(x)
    sort(l)
    print l

    
