a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

if(a>=b and a>=c):
    print("first no is largest: ",a)
elif(b>=c):
    print("second no is largest:",b)
else:
    print("third no is greatest",c)