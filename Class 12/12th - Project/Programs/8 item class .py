class iteminfo():
    def __init__(self,icode=0,iname=0,price=0,qty=0,discount=0):
        self.icode=icode
        self.iname=iname
        self.price=price
        self.qty=qty
        self.discount=discount
        self.items=[]
        
    def Buy(self):
        self.icode=int(input("Enter item_code: "))
        self.iname=str(input("Enter item_name: "))
        self.price=eval(input("Enter price: "))
        self.qty=eval(input("Enter Quantity: "))
        print
        self.items.append([self.icode,self.iname,self.price,self.qty])
        
    def Find_disc(self):
        for i in range (len(self.items)):
            if self.items[i][3]<=10:
                self.discount=0
                self.netprice=((self.price*self.qty)-self.discount)
                self.items[i].append(["Net Price->",self.netprice])

            if self.items[i][3]>10 and self.items[i][3]<20:
                self.discount=15
                self.netprice=((self.price*self.qty)-self.discount)
                self.items[i].append(["Net Price->",self.netprice])
                
            if self.items[i][3]>=20:
                self.discount=20
                self.netprice=((self.price*self.qty)-self.discount)
                self.items[i].append(["Net Price->",self.netprice])
            
    def show_all(self):
        print self.items
        
obj=iteminfo()
n=int(input("Enter No. of Items :-"))
print
for i in range (n):
    obj.Buy()
    obj.Find_disc()
obj.show_all()
        

        
