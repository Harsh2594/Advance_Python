#Chaining Decorators
#In simpler terms chaining decorators means decorating a function with multiple decorators.
def decor1(func):
  def inner1():
    x = func()
    return x * x
  return inner1

def decor(func):
  def inner():
    x = func()
    return 2*x
  return inner

#num = decor1(decor(num)) this function call return inner1 function definition, OR
@decor1 
@decor  
def num():
  return 10

#num2 = decor(decor1(num)) this function call return inner function definition, OR
@decor 
@decor1 
def num2():
  return 10

print(num())
print(num2())