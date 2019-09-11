class society():
    def __init__(self,so=0,hno=0,nom=0,inc=0,flat=0):
        self.so=so
        self.hno=hno
        self.nom=nom
        self.inc=inc
        self.falt=flat
    def inputdata(self):
        self.so=input("Enter the name of society ")
        self.hno=input("Enter the house number ")
        self.nom=input("Enter the number of members ")
        self.inc=int(input("Enter the income "))
    def allocateflat(self):
        if self.inc>=25000:
            self.flat='A'
        if 20000<=self.inc<25000:
            self.flat='B'
        if self.inc>=15000 and self.inc<20000:
            self.flat='C'
        if self.inc<15000:
            self.flat='D'
    def show(self):
        print
        print "House No.:-",self.hno
        print "Society:-",self.so
        print "Number of Members:-",self.nom
        print "Income:-",self.inc
        print "Flat Type:-",self.flat
a=society()
a.inputdata()
a.allocateflat()
a.show()
