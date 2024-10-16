#Decorators definition:
#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, 
#without permanently modifying it. 
# it allows programmers to modify the behaviour of a function or class.

def welcome(func):
  def wrapper(*args,**kwargs):
    print("Welcome to Decorators.com")
    func(*args,**kwargs)
    print("Thanks for visit")
  return wrapper  

#Method1:
#@welcome
def user(name, greets='Welcome '):
  print(f"{greets} {name}")
#Method2:
#user = welcome(user)
user('harsh')