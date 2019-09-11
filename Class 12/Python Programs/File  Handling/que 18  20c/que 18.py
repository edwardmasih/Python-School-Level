name=str(input("Enter File name :- "))
fh=open(name+".txt","r+")
xx=open("Temp.txt","w+")
a=fh.readlines()
print("Number Of Line The TXT file contains :-",len(a))
print("---------------------------------------------------")
fh.seek(0)
word=input("Enter The Alphabet To Search In File :- ")
print("---------------------------------------------------")
c=1
line=" "
while line :
    line=fh.readline() ## Prints The Line
    list=line.split() ## Converts It Into Alag Alphabet In List
    if word in list:
        d=0
        for i in list :
            if i==word:
                d=d+1
        print(line)
        print("Found At line Number :-",c," & ",d," Number Of Times")
        print("\n")
        xx.write("Found At line Number :- "+str(c)+" & "+str(d)+" Number Of Times"+"\n")
    c=c+1
fh.close()
xx.close()
            

    
