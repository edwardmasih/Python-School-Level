import os
def fileDEL(word):
    file = open("test.txt","r")
    newfile = open("new.txt","w")
    line=" "
    while line:
        line = file.readline()
        if word in line :
            lst=line.split()
            print(lst)
            for i in range (len(lst)):
                if lst[i]==word:
                    del (lst[i])
                    break
            
word=input("Enter the WOr To Be deleted :- ")
fileDEL(word)
newfile.write(line)
file.close()
newfile.close()
os.remove("test.txt")
os.rename("new.txt","test.txt")
