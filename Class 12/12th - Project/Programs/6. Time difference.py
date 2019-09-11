print "Program to find Diff. of two times in HH:MM:SS (T1>T2)"
print "First Time Given Should Be Bigger Than Second"
print
class timediff():
    hr=0
    min=0
    sec=0
    def set(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
        
    def show(self):
        print self.hr,"hr",self.min,"min",self.sec,"sec"
    def diff(self,timediff):
        self.hr=self.hr-timediff.hr
        self.min=self.min-timediff.min
        self.sec=self.sec-timediff.sec
        while self.sec<0:
            self.min=self.min-1
            self.sec=60+self.sec
            while self.min<0:
                self.hr=self.hr-1
                self.min=self.min+60
        while self.sec>=60:
            self.min=self.min+1
            self.sec=self.sec-60
            while self.min>=60:
                self.hr=self.hr+1
                self.min=self.min-60
    
c1=timediff()
c2=timediff()
c1.set(int(input("enter the hour :- ")),int(input("enter the minute :- ")),int(input("enter the sec :- ")))
print
c2.set(int(input("enter the hour :- ")),int(input("enter the minute :- ")),int(input("enter the sec :- ")))
c1.diff(c2)
c1.show()
        


    
                                      
