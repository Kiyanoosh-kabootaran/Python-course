# super() = Funtion used in child class to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods

class Shape:
  def __init__(self, color, is_filled):
    self.color = color
    self.is_filled = is_filled

  def describe(self):
    print(f"it is {self.color} and {'filled' if {self.is_filled} else 'not filled'}")

class Circle(Shape):
  def __init__(self, color, is_filled, radius):
    super().__init__(color, is_filled)
    self.radius = radius
  
  def describe(self):
    print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
    super().describe()

class Square(Shape):
  def __init__(self, color, is_filled, width):
    super().__init__(color, is_filled)
    self.width = width
  
  def describe(self):
    print(f"it is a square with an area of {self.width * self.width}cm^2")

class Triangle(Shape):
  def __init__(self, color, is_filled, width, height):
    super().__init__(color, is_filled)
    self.width = width
    self.height = height

circle = Circle(color="red", is_filled=True, radius=4.5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="blue", is_filled=False, width=6, height=8)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius} cm")

print("**********************")

print(square.color)
print(square.is_filled)
print(f"{square.width} cm")

print("**********************")

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width} cm")
print(f"{triangle.height} cm")

print("**********************")

circle.describe() # it points to the child's describe which is then points to the parent's describe
square.describe() # it points to the parent describe

