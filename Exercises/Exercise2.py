# Shopping cart program

item = input("what item would you like to buy? : ")
price = float(input("How much is it? : "))
quantity = int(input("How many do you want? : "))

total = price * quantity

print(f"You have bought {quantity} x {item}s")
print(f"Your total is : ${total}")