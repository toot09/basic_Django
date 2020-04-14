# Class
class Car():
  def __init__(self, **kwargs):
    # Properties
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    # Keyword Argument initialize
    self.color = kwargs.get("color","black")
    self.price = kwargs.get("price", "$45,000")
    
  # Method : In Python, All Method has itselves instance
  def start_method(self):
    print(self.doors)
    print("I started at method in class")
  
  # override
  def __str__(self):
    return f"Car with {self.wheels} wheels"

# Extend
class Convertible(Car):

  def __init__(self, **kwargs):
    # super() calls Parents class
    super().__init__(**kwargs)
    self.time = kwargs.get("time",10)

  def take_off(self):
    return "taking off"
  def __str__(self):
    return f"Car with no roof"

# Function
def start_function():
  print("I started at function")

# Instance
porche = Car(color = "Yellow", price = "$60,000")
porche.start_method()

# keyword arguments
# 1. Setting kwargs
print(porche.color, porche.price)
# 2. No setting kwargs 
hyundai = Car()
print(hyundai.color, hyundai.price)

# heritate
mini = Convertible(color = "Blue")
print(mini.take_off())
print(mini.color, mini.price)
#print(porche.taking_off())
print(mini)
print(hyundai)