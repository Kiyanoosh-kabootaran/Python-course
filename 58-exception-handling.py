# expection = An event that interrupts the flow of a program 
#             (ZeroDivisionErrror, TypeError, ValueError)
#             1.try 2.except 3.finally
try:
  number = int(input("Enter a number!: "))
  print(1 / number)

except ZeroDivisionError:
  print("You can't devide by zero")

except ValueError:
  print("Enter Only numbers Please!")

except Exception:
  print("Somthing went wrong!")

finally:
  print("Do some cleanup here")
