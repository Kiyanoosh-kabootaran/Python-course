# conditional expression = A one line shortcut for the if-else statement (ternary operator)
# print or assign one of two values based on a condition
# X if condition else Y

num1 = -5
num2 = 6
a = 45
b = 33
age = 23
temperature = 30
user_role = "admin"

print("Positive" if num1 > 0 else "Negative")

result = "EVEN" if num2 % 2 == 0 else "ODD"
print(result)

max_num = a if a > b else b   #45
min_num = a if a < b else b   #33
print(max_num)
print(min_num)

status = "Adult" if age >= 18 else "Child"
print(status)

wheather = "Hot" if temperature > 20 else "Cold"
print(wheather)

access_level = "Full acces" if user_role == "admin" else "Limited access"
print(access_level)