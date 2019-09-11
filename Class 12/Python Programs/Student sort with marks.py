class subject ():
    def __init__(self):
        x=[]
        self.students=[]
    def addstudents(self):
        n=int(input("Enter No. Of Students :- "))
        for i in range (n):
            self.name=input("Enter Name :- ")
            self.rno=input("Enter Roll No. :- ")
            self.marks=input("Enter Total Marks :- ")
            print()
            self.students+=[[self.name,self.rno,self.marks]]
        print("ORIGINAL LIST :- ",self.students)
    def final(self):
        v=len(self.students)
        for i in range(v):
            minpos=i
            for j in range(i+1,v):
                if self.students[j][2]>self.students[i][2]:
                    minpos=j
                    temp=self.students[minpos]
                    self.students[minpos]=self.students[i]
                    self.students[i]=temp
        print()
        print("SORTED LIST :- ",self.students)
a=subject()
a.addstudents()
a.final()





    
    

