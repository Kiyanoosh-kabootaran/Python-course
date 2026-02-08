age = int(input("Enter your age: "))

if age >= 100:
  print("You are too old to signup! ")
elif age >= 18:
  print("You are signedup! ")
elif age < 0:
  print("You are not born yet! ")
else:
  print("You must be +18 to signup! ")
