#('weeks', 604800)
#('days', 86400)
#('hours', 3600)
#('minutes', 60)
#('seconds', 1)

class time ():
    def __init__(self,days=0,hour=0,minute=0,sec=0):
        self.days=days
        self.hour=hour
        self.minute=minute
        self.sec=sec


    def setTime(self):
        self.sec = int( input ('Enter the number of seconds: '))
        while self.sec>=60:
            self.sec-=60
            self.minute+=1
            while self.minute>=60:
                self.minute-=60
                self.hour+=1
                while self.hour>=24:
                    self.hour-=24
                    self.days+=1
        
    def show(self):
        print self.days,"days:",self.hour, 'hours :', self.minute, 'min :', self.sec, "seconds"
obj=time()
obj.setTime()
obj.show()
        
        
