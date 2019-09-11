m = int(input('Enter number of terms upto which you want triplets = '))

for a in range(1, m):
    for b in range(a, m):
        for c in range(b, m):
            if (a**2 + b**2 == c**2):
                print(a, b, c)
                
