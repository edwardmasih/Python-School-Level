import pickle
fh=open("roman.data","wb+")
dic={}
n=int(input("Enter No. Of Terms  :-  "))
print()
for i in range(n):
    rom=str(input("Enter Number in roman :-"))
    dec=int(input("Enter Number in Decimal :-  "))
    dic[dec]=rom
print()
print("Final Dictonary :-  ",dic)
pickle.dump(dic,fh)
fh.close()
print()

a=list(dic.keys())
n=int(input("Enter Decimal To Get It In Roman :- "))
for i in range (len(a)):
    if n==a[i]:
        print("Number in Roman is :-",dic[n])
if n!=a[i]:
    print("Error!! Given  No. Not Found !! Now Get The Hell Out Of Here !!")


