fh=open("TextF.txt","r+")
v="aeiouAEIOU123 4567890{}[]"
a=list(v)
print(a)
txt=fh.read()
c=0
for i in txt:
    if i in v :
        c=c+1
print(c)

print("____________________________________________")


        
    
