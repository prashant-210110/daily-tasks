#NameError: name  is not defined
#TypeError: unsupported operand type(s) for /: 'str' and 'str'
#KeyError: 104 not in the dictionary
#AttributeError: 'dict' object has no attribute 'add'
#IndexError: list index out of range
# try except else finally raise
#python exception handeling


'''try:
  x=int(input("enter required number"))
  y=int(input("enter required number"))
  print("the result is",int(x/y))
except:
  pass
  print("error :arithemetic operation ignored.pass block")
  pass
else:
  print("successfully done ")'''


'''  def age(age):
      assert age >= 18, "age must not be less then 18 years"  # if the conditions false only this line will execute
      print("you are allowed to vote", age)
      print("thanks for voting...........")
  age(17)'''



'''try:
  s=int(input("enter number"))
  a=int(input("enter number"))
  c=s/a
  print("the value is:",c)
except ZeroDivisionError:
  print("zero division error")
except ValueError:
  print("value error")
except Exception:
  print("exception")'''



'''try:
  s=int(input("enter number"))
  a=int(input("enter number"))
  c=s/a
  print("the value is:",c)
except Exception as e:                #makes asingle line
  print("exception",e)'''



'''from ast import excepthandler
try:
  print("try block")            #it will execute when condition is true
except:
  print("except block")         #it will execute when the try block is fail
else:
  print("else block")           #it wil execute when try block is execute
finally:
  print("finally block")        #it will execute every time
raise               #it is a user defined error'''



