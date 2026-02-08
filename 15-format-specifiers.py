# format specifiers = {value : flags} format a value based on what flags are inserted 

price1 = 320001.14548 
price2 = -45.845
price3 = 0.254

print(f"Price 1 is ${price1:10}") # it is default for : print(f"Price 1 is ${price1:>10}")
print(f"Price 1 is ${price1:<10}")
print(f"Price 1 is ${price1:^10}")
print(f"Price 1 is ${price1:+}")
print(f"Price 1 is ${price1:,}")
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:.2f}")
  