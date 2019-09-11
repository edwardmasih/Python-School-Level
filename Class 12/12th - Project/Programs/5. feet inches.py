class lensum():
    ft=0
    In=0
    def set(self,feet,inch):
        self.ft=feet
        self.In=inch
    def show(self):
        print self.ft,"feet",self.In,"inches"
    def add(self,lensum):
        self.In=self.In+lensum.In
        self.ft=self.ft+lensum.ft
        while self.In>=12:
            self.ft=self.ft+1
            self.In=self.In-12
    
c1=lensum()
c2=lensum()
c1.set(int(input("enter the feet :- ")),int(input("enter the inch:- ")))
c2.set(int(input("enter the feet:- ")),int(input("enter the inch :- ")))
c1.add(c2)
c1.show()
        
