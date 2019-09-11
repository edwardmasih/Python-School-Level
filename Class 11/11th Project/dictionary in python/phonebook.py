phonebook=dict()

n=int(input("Enter total number of friends "))
i=1
while i<=n:
    a=input("enter name ")
    b=input("enter phone number ")
    phonebook[a]=b
    i=i+1
print("Name","\t","Number")
for i in phonebook:
    print(i,"\t",phonebook[i])


#to find the name and number of particular person
name=input("enter name to search ")
l=phonebook.keys()
for i in l:
    if (i==name):
        print ("Phone number = ",phonebook[i])


