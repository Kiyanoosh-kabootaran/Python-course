# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

  def __init__(self, name, position):
    self.name = name
    self.position = position

# get_info is an instance method
  def get_info(self):
    return f"{self.name} = {self.position}"
# is_valid_position is a static method
  @staticmethod
  def is_valid_position(position):
    valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
    return position in valid_position
  
employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(Employee.is_valid_position("computer scientist"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
  
