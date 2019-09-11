class train :
    def __init__(self,train_no,name,starting_station,destination,departure_time,arrival_time):
        self.train_no=train_no
        self.name=name
        self.starting_station=starting_station
        self.destination=destination
        self.departure_time=departure_time
        self.arrival_time=arrival_time  
    def getdata(self):
        print("Train No. :- ",self.train_no)
        print("Train Name :- ",self.name)
        print("Train starting_station :- ",self.starting_station)
        print("destination :- ",self.destination)
        print("departure_time :- ",self.departure_time)
        print("arrival_time :- ",self.arrival_time)
        

class passenger :
    def __init__(self,ticket_no,Pname,gender,age,address,phone_no):
        self.ticket_no=ticket_no
        self.Pname=Pname
        self.gender=gender
        self.age=age
        self.address=address
        self.phone_no=phone_no    
    def getdata1():
        print("Ticket No:- ",self.ticket_no)
        print("gender :- ",self.gender)
        print("Age:- ",self.age)
        print("Address :- ",self.address)
        print("Phone No:- ",self.phone_no)
    def display():
        for i in range (0,5):
            if xyz==x[0]:
                return passenger.getdata1()
            
        
    
n=int(input("Enter No. Of Passengers :-"))
print "Give Info OF",n," Passengers" 
for j in range (5):
    c="Enter Ticket Number :- ","Enter Name :- ","Enter Gender :- "
for i in range(0,n):
    e=[i for i in range (0,3)]
    for i in range (0,3):
        e[i]=input(c[i])
    print e
    print
    
print "Your List is ",a
        
        
xyz=int(input("Enter the Ticket No. to get Details :-"))
      
