file=open('quiz.by','rb+')
import pickle
l=list(pickle.load(file))
print "GET READY FOR THE QUIZ"
print
print "JUST TYPE THE A, B or C FOR YOUR CHOICE OF ANSWER"
print
print
def quiz():
        for i in range(len(l)):
            for j in range (len(l[i])-1):
                print l[i][j]
            a=raw_input("Enter Your Choice : ")
            print
            if a==l[i][-1]:
                print("Right Answer")
                print

            if a!=l[i][-1]:
                print("Sorry Wrong Answer")
                print("Option "+l[i][-1]+ " is the right answer")
            
                
quiz()
