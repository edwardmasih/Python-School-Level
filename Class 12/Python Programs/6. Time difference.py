print("Program to find Diff. of two times in HH:MM:SS (T1>T2)")

h1=int(input("Enter hours of T1:"))
m1=int(input("Enter minutes of T1:"))
s1=int(input("Enter seconds of T1:"))
print("T1 is =>",h1,":",m1,":",s1)
print()

h2=int(input("Enter hours of T2:"))
m2=int(input("Enter minutes of T2:"))
s2=int(input("Enter seconds of T2:"))
print("T2 is =>",h2,":",m2,":",s2)
print()

h3=h1-h2

if(m2>m1):
    m0=m2-m1
    m3=60-m0
else:
    m3=m1-m2

if(s2>s1):
    s0=s2-s1
    s3=60-s0
else:
    s3=s1-s2


print("Time Difference is :-")    
print("T3 is =>",h3,":",m3,":",s3)


