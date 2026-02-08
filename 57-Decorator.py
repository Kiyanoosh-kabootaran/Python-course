# Decorator = A function that extends the behavior of another funciton 
#             w/o modifying the base fucntion
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

# We need wrapper function to add sprinkle when we call get_ice_cream

def add_sprinkeles(func):
  def wrapper(*args, **kwargs):
    print("You add sprinkles 🧁")
    func(*args, **kwargs)

  return wrapper

def add_fudge(func):
  def wrapper(*args, **kwargs):
    print("You add fudge 🍫")
    func(*args, **kwargs)
  
  return wrapper


@add_sprinkeles
@add_fudge
def get_ice_cream(flavor):
  print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("vanilla")