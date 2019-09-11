s=[]
c="y"
while(c=="y"):
    print ("Enter 1. To  PUSH ")
    print ("Enter 2. To  POP ")
    print ("Enter 3. To  PEEK ")
    print ("Enter 4. To  Display ")
    print("________________________________________________________________")
    choice=int(input("Enter Your Choice :- "))
    if (choice==1):
            a=int(input("Enter The Element To Drop In QUEUES :-"))
            s.append(a)
    elif(choice==2):
        if (s==[]):
            print("ERROR !! Queue Empty")
        else:
            print ("Element Deleted is ",s.pop(0))
    elif(choice==3):
        print("FIRST ELEMENT :- ",s[0])
    elif(choice==4):
        for i in range (len(s)):
            print(s[i])
    else:
        print("Wrong Input")
    print()
    c=input("Enter 'y' To Continue :- ")
    print("________________________________________________________________")
if c!='y':
    print("Bye")
    quit
