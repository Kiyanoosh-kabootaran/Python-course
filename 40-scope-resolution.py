# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Eclosed -> Global -> Built-in

'''
def func1():
  a = 1                       # a is local variable to func1
  print(a) 
'''
'''-------------------------------------------------------------------'''
'''
def func1():
  x = 1  

  def func2():
    print(x)  # it uses x in enclosed scope (x=1) because there is no local x
  func2()        

func1()          
'''
'''-------------------------------------------------------------------'''
'''
def func1():
  print(x)   # it uses x in global scop (x=3)

def func2():
  print(x)

x = 3 

func1()
func2()
'''
'''-------------------------------------------------------------------'''
'''
from math import e

def func1():
  print(e)              # e is built in variable

func1()
'''
'''-------------------------------------------------------------------'''
'''
from math import e

def func1():
  print(e)              # it will use e = 3 because global variable has more priority than buitl-in

e = 3 

func1()
'''