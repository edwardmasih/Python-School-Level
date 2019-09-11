import pickle
class student:
    def __init__(self,rno=0,name=0,marks=0,add=0,phone=0,dob=0,cls=0,sec=0,sex=0):
        self.rno=rno
        self.name=name
        self.marks=marks
        self.add=add
        self.phone=phone
        self.dob=dob
        self.cls=cls
        self.sec=sec
        self.sex=sex
    def get(self):
        self.rno=int(raw_input( "Enter Roll No. :- "))
        self.name=raw_input ("Enter Name :- ")
        self.sex=raw_input("Enter Sex :- ")
        self.dob=raw_input("Enter Date Of Birth :- ")
        self.cls=int(raw_input("Enter class :- "))
        self.sec=raw_input("Enter Section :- ")
        self.marks=int(raw_input ("Enter Total Marks :- "))
        self.add=raw_input("Enter Address :- ")
        self.phone=int(raw_input("Enter Contact Number :- "))
    def show(self):
        print self.rno,"\t",self.name,"\t",self.sex,"\t",self.dob,"\t",self.cls,"\t",self.sec,"\t",self.marks,"\t",self.add,"\t",self.phone

fh=open("StudentsRecord.data","wb+")
obj=student()
n=int(raw_input("Enter The Number Of Students :- "))
print

stud=[]
for i in range (n):
    obj.get()
    stud.append([obj.rno,obj.name,obj.sex,obj.dob,obj.cls,obj.sec,obj.marks,obj.add,obj.phone])
    print
    
print
print "Details OF All Student"
print
k=["Roll No.","Name","Sex","DOB","cls","Section","Marks","Address","Phone"]
for i in stud:
    for j in range (len(k)):
        print k[j],'\t','\t',i[j]
    print
pickle.dump(stud,fh)
print

#Student Search

x=int(raw_input ("Enter the Roll No. To Search :- " ))
print
for i in range (len(stud)):
    if x == stud[i][0]:
        print "Search Found "
        print
        for j in range (len(k)):
            print k[j],'\t',stud[i][j]
if x != stud[i][0]:
    print "Search Not Found! Bye"
print

#Finding Topper
print "Finding Topper"
m=[]
for i in range (len(stud)):
    m.append(stud[i][6])
l=max(m)
for i in range (len(stud)):
    if l==stud[i][6]:
        print "The Topper IS "
        print "Roll No. =",stud[i][0]," Name =",stud[i][1]," Marks =",stud[i][2]

fh.close()








