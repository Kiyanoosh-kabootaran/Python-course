# Inheritance = Allows a class to inherit attributes and methods from another clss
#               Helps with code reusability and extensibility
#               Class Child(Parent)

class Animals:
  def __init__(self, name):
    self.name = name
    self.is_alive = True

  def eat(self):
    print(f"{self.name} is eating")

  def sleep(self):
    print(f"{self.name} is sleeping")

class Dog(Animals):
  def speak(self):
    print("WOOF!")

class Cat(Animals):
  def speak(self):
    print("MEOW!")

class Mouse(Animals):
  def speak(self):
    print("SQUEEK!")

dog = Dog("Scoby")
cat = Cat("Garfield")
mouse = Mouse("Micky")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

dog.speak()
cat.speak()
mouse.speak()
cat.sleep()