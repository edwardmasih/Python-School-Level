file=open('quiz.by','wb+')
import pickle

class que ():
    def __init__(self):
        x=[]
        self.que=[]
    def addque(self):
        n=int(input("Enter No. Of Questions :- "))
        print
        print
        for i in range (n):
            self.quest=raw_input("Enter Question :- ")
            self.A=raw_input("Enter Option A :- ")
            self.B=raw_input("Enter Option B :- ")
            self.C=raw_input("Enter Option C :- ")
            self.correct=raw_input("Enter the option which is correct : ")
            print
            self.que+=[["Question "+self.quest,"Option A : "+self.A,"Option B : "+self.B,"Option C : "+self.C,self.correct]]
        #print("ORIGINAL LIST :- ",self.que)
    def final(self):
       pickle.dump(self.que,file)
    
a=que()
a.addque()
print
a.final()
print
print
print
file.close()








