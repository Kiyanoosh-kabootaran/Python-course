# Python compund interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0 :
  principle = int(input("Enter the principle amount: "))
  if principle <= 0:
    print("Time can't be less than or equal to zero")

while rate <= 0 :
  rate = int(input("Enter the interest rate: "))
  if principle <= 0:
    print("interest rate can't be less than or equal to zero")

while time <= 0 :
  time = int(input("Enter the time it years: "))
  if time <= 0:
    print("Time can't be less than or equal to zero")

total = principle * pow((1 + rate / 100) , time)
print(f"Balance after {time} year/s: ${total:.2f}")
  