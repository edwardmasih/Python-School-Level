def count (a,x):
    c=0
    for i in range (0,len(a)):
        if (a[i]==x):
            c=c+1
    if (c>=1):
        print(c," times")
    else :
        print("-1")
n=int(input("Enter The No. Of Elements in List :- "))
a=[i for i in range (n)]
print ("Enter the Elements one after the other :- ")
for i in range (n):
    a[i]=int(input())
print("Your List is ",a)
x=int(input("Enter The Element To find in List :- "))
p=count(a,x)
