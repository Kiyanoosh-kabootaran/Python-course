# keyword arguments =  an argument preceded by an identifier
#                      helps with readability
#                      order of arguments doesn't matter
#                      1. positional, 2.default, 3. KEYWORD, 4.arbitary


def hello(greeting, title, first, last):
  print(f"{greeting} {title} {first} {last}")

hello("Hello", title="Mr.", last="Kabootaran", first="Kiyanoosh")


# end, sep are also a keyword argument
'''
for x in range(1,11):
  print(x, end=" ")
'''

# print("1","2","3","4","5","6","7", sep="-")