x=int(input("Enter First Number="))
q=int(input("Enter 1 for Addition,2 for Substraction,3 for Multiplication and 4 for Dividion="))
# print("Enter 1 for Addition,2 for Substraction,3 for Multiplication and 4 for Dividion",q)
y=int(input("Enter Second Number="))
if q==1:
    print("Addition of Two Numbers=",int(x+y))
elif q==2:
    print("Substraction of Two Numbers=",int(x-y))
elif q==3:
    print("Multiplication of Two Numbers=",int(x*y))
elif q==4:
    print("Division of Two Numbers=",int(x/y))
else:
    print("Invalid Input")