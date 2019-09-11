s=[]
c="yes"
while(c=="yes"):
    print ("Enter 1. To  PUSH ")
    print ("Enter 2. To  POP ")
    print ("Enter 3. To  PEEK ")
    print ("Enter 4. To  Display ")
    print("________________________________________________________________")
    choice=int(input("Enter Your Choice :- "))
    if (choice==1):
            a=int(input("Enter The Element To Drop In Stack :-"))
            s.append(a)
    elif(choice==2):
        if (s==[]):
            print("ERROR !! Stack Empty")
        else:
            print ("Element Deleted is ",s.pop())
    elif(choice==3):
        print("TOPMOST ELEMENT :- ",s[-1])
    elif(choice==4):
        for i in range ((len(s)-1),-1,-1):
            print(s[i])
    else:
        print("Wrong Input")
    print()
    c=input("Enter 'yes' To Continue :- ")
    print("________________________________________________________________")
if c!='yes':
    print("Bye")
    quit
