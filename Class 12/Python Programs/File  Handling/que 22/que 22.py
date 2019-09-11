import pickle
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
       print(self.code,"\t",self.name,"\t",self.price,"\t",self.qty)
    def search(self):
        n=input("Enter Item Code To Get Details :- ")
        v=len(self.items)
        for i in range (v):
            if n==self.code[i][0]:
                print (self.code[i][0],"\t",self.name[i][1],"\t",self.price[i][2],"\t",self.qty[i][3])
                
            else:
                print("Wrong input !")
    def update (self):
        x=input("Enter Item Code To Update It :- ")
        v=len(self.items)
        for i in range (v):
            if n==self.code[i][0]:
                self.name=input("Enter New Item Name :- ")
                self.price=input("Enter New Item Price :- ")
                self.qty=input("Enter New item Quantity :-")
                self.items+=[[self.name,self.price,self.qty]]

fh=open("items.data","wb+")
obj=item()
n=int(input("Enter The No. Of Items :- "))
print("-----------------------------------------------------------------------")
for i in range (n):
    obj.get()
    pickle.dump(obj,fh)
fh.close()

file=open("items.data","rb+")        
try:
    while True:
        obr=pickle.load(file)
        obr.show()
except EOFError:
    pass
file.close()

x=open("items.data","wb+")
abc=pickle.load(x)
abc.search()
abc.update()
x.close()


        
        
            
    
