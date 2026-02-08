#Python weight convertor

weight = float(input("Enter the wight : "))
unit = input("enter the unit (K / L): ")

if unit == "K":
  weight = weight * 2.205
  unit = "Lbs"
  print(f"your weight is {round(weight,2)} {unit}")
elif unit == "L":
  weight = weight / 2.205
  unit = "Kg"
  print(f"your weight is {round(weight,2)} {unit}")
else:
  print(f"{unit} is not valid")

