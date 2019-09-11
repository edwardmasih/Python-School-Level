class item():
    def __init__ (self,code=0,name=0,price=0,qty=0):
        self.items=[]
        self.code=code
        self.name=name
        self.price=price
        self.qty=qty
    def get(self):
            self.code=input("Enter Item Code :- ")
            self.name=input("Enter Item Name :- ")
            self.price=input("Enter Item Price :- ")
            self.qty=input("Enter item Quantity :-")
            self.items+=[[self.code,self.name,self.price,self.qty]]
    def show(self):
        for i in range (len(self.items)):
            print(str(self.items[i]))
    def search(self):
        n=input("Enter Item Code To Get Details :- ")
        v=len(self.items)
        for i in range (v):
            if n==self.items[i][0]:
                print (self.items[i][0],"\t",self.items[i][1],"\t",self.items[i][2],"\t",self.items[i][3])
                
    def update (self):
        x=input("Enter Item Code To Update It :- ")
        v=len(self.items)
        for i in range (v):
            if x==self.items[i][0]:
                self.items[i][1]=input("Enter New Item Name :- ")
                self.items[i][2]=input("Enter New Item Price :- ")
                self.items[i][3]=input("Enter New item Quantity :-")
                self.items+=[[self.name,self.price,self.qty]]
                self.items.pop(i+1)
                print(self.items)
               


obj=item()
n=int(input("Enter The No. Of Items :- "))
print("-----------------------------------------------------------------------")
for i in range (n):
    obj.get()
    print()
obj.show()
obj.search()
obj.update()


