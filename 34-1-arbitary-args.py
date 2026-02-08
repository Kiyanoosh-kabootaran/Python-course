# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#             * unpacking operator
# 1. positional, 2.default, 3. keyword, 4. ARBITARY

'''
def add(*nums):
  total = 0
  for num in nums:
    total += num

  return total
'''
# print(add(1,5,4,45,54,74.5))

def display_name(*args):
  for arg in args:
    print(arg, end=" ")

display_name("Dr.","Kiyanoosh","J","Kabootaran")

