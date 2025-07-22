a=int(input("enter the value"))
b=int(input("enter the value"))
try:
    print("the addition of",a,"and",b,"is",(a+b))
    print("the subtraction of",a,"and",b,"is",(a-b))
    print("the multiplication of",a,"and",b,"is",(a*b))
    print("the division of",a,"and",b,"is",(a/b))
    print(a,"raises to the power of",b,"is",(a**b))
    print("the floor division of",a,"and",b,"is",(a//b))
    print("the moduls of",a,"and",b,"is",(a%b))
except ZeroDivisionError:
    print("we could not perform division using 0")
