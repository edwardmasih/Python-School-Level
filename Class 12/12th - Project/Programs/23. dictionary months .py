cal=dict ()
print "NOTE !! Enter All Alphabets In Small Letters"
print
n=12
i=1
while i<=n:
    a=input("Enter The MOnth :-")
    b=int(input("Enter No OF Days :-"))
    print
    cal[a]=b
    i=i+1

print "Month","\t", "No. Of The Days"
for i in cal:
    print(i,"\t",cal[i])
    
print
print "Dictionary In Asecnding Order By Month Name"
print "Month","\t", "No. Of The Days"
l=(list(cal.keys()))
l.sort()
for i in l:
    print i,"\t",cal.get(i)




