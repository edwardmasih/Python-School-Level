def replace(s1,s2,n1,n2):
    f1=open(n1,"r")
    f2=open(n2,"w")
    a=f1.read()
    newtxt=a.replace(s1,s2)
    f2.write(newtxt)
    f1.close()
    f2.close()
replace ("*","&","que19.txt","New.txt")
