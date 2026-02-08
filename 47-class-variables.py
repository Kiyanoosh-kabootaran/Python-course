# class variables = shared among all instance of a class
#                   Defined outside the constructor
#                   Allow you to share date among all objects created from that class

class Students:

  class_year = 2024
  num_students = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Students.num_students += 1

student1 = Students("Spongebob", 30)
student2 = Students("Patrick", 35)
student3 = Students("Squidward", 55)
student4 = Students("Sandy", 27)

#print(student1.name)
#print(student1.age)
#print(Students.class_year)
#print(Students.num_students)

print(f"My graduating class of {Students.class_year} has {Students.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)