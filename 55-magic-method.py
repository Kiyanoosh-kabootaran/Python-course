# Magic methods = Dunder methods (double underscore) __init__,__str__,__eq__
#                 They are automatically called by many of Python's built-in operations
#                 They allow developers to define or customize the behavior of objects

class Book:

  def __init__(self, title, author, num_pages):
    self.title = title
    self.author = author
    self.num_pages = num_pages

  def __str__(self):
    return f"'{self.title}' by {self.author}"
  
  def __eq__(self, other):
    return self.title == other.title and self.author == other.author
  
  def __lt__(self, other):
    return self.num_pages < other.num_pages
  
  def __gt__(self, other):
    return self.num_pages > other.num_pages
  
  def __add__(self, other):
    return f"{self.num_pages + other.num_pages} pages"
  
  def __contains__(self, keyword):
    return keyword in self.author or keyword in self.title
  
  def __getitem__(self, key):
    if(key == 'author'):
      return self.author
    elif(key == 'title'):
      return self.title
    elif(key == 'pages'):
      return self.num_pages
    else:
      return f"key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion, The Witch and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 350)

print(book1) # __str__
print(book1 == book4) # __eq__
print(book1 < book4) #__lt__
print(book1 > book4) #__gt__
print(book1 + book2) #__add__
print("Harry" in book2) # __contains__
print(book4['author']) # __getitem__