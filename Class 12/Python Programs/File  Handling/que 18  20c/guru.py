name=str(input("Enter File name :- "))
fh=open(name+".txt","r+")
n=input("Enter The Elemnt To Be Sarched :- ")
while True:
   line=fh.readline()
   if n in line:
       print(line)
   
fh.close()
