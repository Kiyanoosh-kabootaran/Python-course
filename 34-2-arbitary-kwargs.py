'''
def print_address(**kwargs):
  for value in kwargs.values():
    print(value)
'''

'''
def print_address(**kwargs):
  for value in kwargs.keys():
    print(value)
'''

def print_address(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}:{value}")

print_address(street="azadi",
              city="Tehran",
              state="Tehran",
              zip="54698")