fh=open("TextF.txt","r+")
v=("a e i o u A E I O U 1 2 3 4 5 6 7 8 9 0 ")
r=fh.readlines()
t=0
for i in (r):
    for j in (i.split()):
        for k in j:
            for h in v:
                if k==h:
                    t=t+1
print(t)
