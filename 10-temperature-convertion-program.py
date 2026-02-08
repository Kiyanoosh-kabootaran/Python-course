unit = input("Is this temperature in celcius or farenheit: (C / F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
  temp = round(temp * (9/5) + 32,2)
  print(f"the temprature is {temp}°F")
elif unit == "F":
  temp = round(temp - 32 * (9/5),2)
  print(f"the temprature is {temp}°C")
else: 
  print(f"{unit} is not a valid measurement")