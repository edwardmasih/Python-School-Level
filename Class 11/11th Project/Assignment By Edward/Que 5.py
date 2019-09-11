# Investment Amount

fav=float(input("Enter The Final Account Value :- "))
i=float(input("Enter The Monthly Interest Rate :- "))
m=float(input("Enter The number Of Months :- "))
Dp=(fav/((1+i)**m))
print ("The Initial Deposit Amount is :- ",Dp)
