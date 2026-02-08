# Iterables = An object/collection that can return its elements one at a time
#             allowing it to be iterated over in a loop

numbers = (1, 2, 3, 4, 5)
fruits = {"apple", "orange", "banana", "coconut"}
name = "Kiyanoosh Kabootaran"
my_dictionary = {"A":1, "B":2, "C":3}

'''
for number in numbers:
  print(number, end="-")
'''
# set object {} is not reversiable
'''
for fruit in fruits:
  print(fruit,end=" ")
'''

'''
for character in name:
  print(character, end= " ")
'''

'''
for key in my_dictionary:
  print(key)
'''

'''
for value in my_dictionary.values():
  print(value)
'''

for key, value in my_dictionary.items():
  print(f"{key} = {value}")