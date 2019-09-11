class Complex:
    r=0
    img=0

    def set (self,r,img):
        self.r=r
        self.img=img

    def show (self):
        print("(",self.r,")","+","(",self.img,"i )",)

    def add(self,Complex):
        self.r=(self.r)+(Complex.r)
        self.img=(self.img)+(Complex.img)

c1=Complex()
c2=Complex()
c1.set(int(input("Enter The real Part :- ")),int(input("Enter The Imaginary Part :-")))
c2.set(int(input("Enter The real Part :- ")),int(input("Enter The Imaginary Part :-")))
c1.add(c2)
c1.show()
