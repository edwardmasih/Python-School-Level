fh=open("myfile.txt","w")
fh.writelines("Neither apple nor pine are in pineapple. Boxing rings are square."+"\n")
fh.writelines("Writers write, but fingers don't fing. Overlook and oversee are opposites. A house can burn up as it burns down. An alarm goes off by going on.")
fh.close()

fh=open("myfile.txt","a")
fh.write("\n"+"Hello Guys")
fh.close()

fh=open("myfile.txt","r")
print(fh.read())
fh.close()
print()

fh=open("myfile.txt","r")
n=int(input("enter the line number to show the line "))
l=fh.readlines()
print (l[n-1])
print()

xx=open("myfile.txt","r")
n=int(len(xx.readlines()))
print(n,"lines")
fh.close()

a=open("myfile.txt","r")
a.seek(10)
print(a.read())
print()

a=open("myfile.txt","r")
l=a.readlines()
print (l[-1])





