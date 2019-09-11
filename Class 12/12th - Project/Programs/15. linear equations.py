class LinearEquation():
    # ax + by = e
    # cx + dy = f

    # x = ((e*d)-(b*f))/((a*d)-(b*c))
    # y = ((a*f)-(e*c))/((a*d)-(b*c))
    def __init__(self,a=0,b=0,c=0,d=0,e=0,f=0,g=0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        
    def geta(self):
        self.a=int(input("Enter The Value Of a :-"))
    def getb(self):
        self.b=int(input("Enter The Value Of b :-"))
    def getc(self):
        self.c=int(input("Enter The Value Of c :-"))
    def getd(self):
        self.d=int(input("Enter The Value Of d :-"))
    def gete(self):
        self.e=int(input("Enter The Value Of e :-"))
    def getf(self):
        self.f=int(input("Enter The Value Of f :-"))
    

    def isSolvable(self):
        if ((self.a*self.d)-(self.b*self.c)) != 0:
            print "Solvable"
        else:
            print "Sorry! This Equation Has No Solution"

            
    def getx(self):
        if ((self.a*self.d)-(self.b*self.c)) != 0:
            x = ((self.e*self.d)-(self.b*self.f))/((self.a*self.d)-(self.b*self.c))
            print "Value Of x :- ",x
        else:
            return False
        
    def gety(self):
        if  ((self.a*self.d)-(self.b*self.c)) != 0:
            y = ((self.a*self.f)-(self.e*self.c))/((self.a*self.d)-(self.b*self.c))
            print "Value Of y :- ",y
        else:
            return False

a=LinearEquation(0,0,0,0,0,0,0)
a.geta()
a.getb()
a.getc()
a.getd()
a.gete()
a.getf()

a.isSolvable()
a.getx()
a.gety()
        
        
