class queue:
    s=[]
    def push(self):
        a=input("Enter any number :")
        queue.s.append(a)
    def display(self):
        l=len(queue.s)
        for i in range(l):
            print (queue.s[i])
    def peek(self):
        if (queue.s==[]):
            print("Queue Empty")
        else:
            print("First Element :- ",queue.s[0])
a=queue()
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
            print ("queue Empty")
        else:
            print ("Deleted element is : ",a.s.pop(0))
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
