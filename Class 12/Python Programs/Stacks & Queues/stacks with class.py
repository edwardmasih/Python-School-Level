class stack:
    s=[]
    def push(self):
        a=input("Enter any number :")
        stack.s.append(a)
    def display(self):
        if (stack.s==[]):
            print("Stack Empty")
        else:
            l=len(stack.s)
            for i in range(l-1,-1,-1):
                print (stack.s[i])
    def peek(self):
        if (stack.s==[]):
            print("Stack Empty")
        else:
            print("Top Most Element :- ",stack.s[-1])
a=stack()
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
            print ("Stack Empty")
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
