class Measure:
    feet=0
    inches=0

    def set (self,feet,inches):
        self.feet=feet
        self.inches=inches

    def show (self):
        print("=> ",self.feet,"Feet","&",self.inches," Inches",)

    def add(self,Measure):
        self.feet=(self.feet)+(Measure.feet)
        self.inches=(self.inches)+(Measure.inches)
        while self.inches >= 12:
            self.feet=self.feet+1
            self.inches=self.inches-12
            

c1=Measure()
c2=Measure()
c1.set(int(input("Enter The Feet Part :- ")),int(input("Enter The Inch Part :-")))
c2.set(int(input("Enter The Feet Part :- ")),int(input("Enter The Inch Part :-")))
c1.add(c2)
c1.show()
