class stacks:
    s=[]
    def push(self):
        z=[]
        n=str(input("Enter Student's Name :- "))
        c=str(input("Enter Student's Class And Section (Class in Roman Numbers): -"))
        dob=input("Enter Student's Date Of Birth (dd/mm//yyyy)(enter slashes too):- ")
        z+=[n,c,dob]
        stacks.s.append(z)
    def display(self):
        l=len(stacks.s)
        for i in range(l-1,-1,-1):
            print (stacks.s[i])
    def peek(self):
        if (stacks.s==[]):
            print("stacks Empty")
        else:
            print("Top Most's Student's Info :- ",stacks.s[-1])
a=stacks()
c="y"
while(c=="y"):
    print ("Enter 1. To  PUSH ")
    print ("Enter 2. To  POP ")
    print ("Enter 3. To  PEEK ")
    print ("Enter 4. To  Display ")
    print("________________________________________________________________")
    choice=int(input("Enter Your Choice :- "))
    if (choice==1):
        a.push()
    elif (choice==2):
        if (a.s==[]):
            print ("stacks Empty")
        else:
            print ("Deleted element is : ",a.s.pop())
    elif (choice==3):
        a.peek()
    elif (choice==4):
        a.display()
    else:
        print("Wrong Input")
    c=input("If You Wanna Continue Enter 'y' :- ")
if c!='y':
    print("Bye")
    quit
