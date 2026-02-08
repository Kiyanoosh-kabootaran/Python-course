# object oriented programing 
# object = A "bundle" of related attributes (variables) and methods (functions)
#            Ex. phone, cup, book
#            You need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object 

class Car:
  def __init__(self, model, year, color, for_sale):
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale

  def drive(self):
    print(f"You drive the {self.color} {self.model}")

  def stop(self):
    print(f"You stop the {self.color} {self.model}")

  def describe(self):
    print(f"{self.year}-{self.color}-{self.model}")

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvettte", 2025, "blue", True)
car3 = Car("Charget", 2026, "yellow", True)

print(car1) # Shows the memory address 

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()

car1.describe()
car2.describe()
car3.describe()