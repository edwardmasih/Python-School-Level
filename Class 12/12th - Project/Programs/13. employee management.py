class employee():
    def __init__(self,eno=0,ename=0,desig=0,basicpay=0,add=0,pno=0):
        self.eno=eno
        self.ename=ename
        self.desig=desig
        self.basicpay=basicpay
        self.add=add
        self.pno=pno
        self.l=[]
    def getdata(self):
        self.eno=input("Enter Employee No. ")
        self.ename=input("Enter Employee Name ")
        self.desig=input("Enter Employee Designation ")
        self.add=input("Enter Employee Address ")
        self.pno=input("Enter Employee Phone No. ")
    def show(self):
        print "Employee Details"
        print self.eno,self.ename,self.desig,self.add,self.pno

   
class salary() :
    def __init__(self,basicpay=0,hra=0,da=0,grosspay=0,pf=0,tax=0):
        self.basicpay=basicpay
        self.hra=hra
        self.da=da
        self.grosspay=grosspay
        self.pf=pf
        self.tax=tax
        
    def getdata1(self):
        self.basicpay=int(input("Enter Employee Basic Pay "))
        
    def calculate (self):
        self.hra = (40/100)*self.basicpay
        self.da = self.basicpay
        self.grosspay=(self.hra+self.da)
        self.pf=(12/100)*self.basicpay
        if self.basicpay>=200000 and self.basicpay<500000:
            self.tax=(10/100)*self.basicpay
        if self.basicpay>=500000 and self.basicpay<1000000:
            self.tax=(20/100)*self.basicpay
        if self.basicpay>=1000000:
            self.tax=(30/100)*self.basicpay
        else :
            self.tax=0
        self.netpay=(self.grosspay+self.pf+self.tax)
        print "NetPay ",round(self.netpay,2)


a=employee()
b=salary()
n=int(input("Enter No. of Employee "))
print
l=[]
for i in range(n):
    l+=[a.getdata(),b.getdata1()]
    print
    a.show()
    b.calculate()
    print
    
