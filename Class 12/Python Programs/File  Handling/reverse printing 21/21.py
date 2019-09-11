fh=open("file.txt","r+")
a=fh.readlines()
x=len(a)
print("Number Of Lines In File :- ",x)
print("----------------------------------------------------------")
print("||Original File||")

for i in a :
    print (i)
print("----------------------------------------------------------")
print("||Reversed File||")
for i in range (x-1,-1,-1):
    print(a[i])

print("----------------------------------------------------------")
print("||Reverse Printing Last line||")
ba=a[-1]
d=ba.split()
for i in range (len(d)-1,-1,-1):
    print(d[i],end=" ")
    
