class Complex():
    r=0
    img=0
    def set(self,real,img):
        self.r=real
        self.img=img
    def show(self):
        print self.r,"+",self.img,"i"
    def add(self,Complex):
        self.r=self.r+Complex.r
        self.img=self.img+Complex.img
    def multi(self,Complex):
        b=self.r*Complex.r-self.img*Complex.img
        c=self.r*Complex.img+Complex.r*self.img
        self.r=b
        self.img=c
c1=Complex()
c2=Complex()
c1.set(int(input("enter the real part")),int(input("enter the imaginary part")))
c2.set(int(input("enter the real part")),int(input("enter the imaginary part")))
print
print "Addition of Two Complex :- "
c1.add(c2)
c1.show()
print

