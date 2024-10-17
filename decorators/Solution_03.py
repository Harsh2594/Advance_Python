#What if a function returns something or an argument is passed to the function?
def hello_decorator(func):
  def inner1(*args,**kwargs):
    print("before Execution")
    # getting the returned value
    returned_value = func(*args,**kwargs)

    print("after Execution")
    #returning the value to the original frame
    return returned_value
  return inner1

@hello_decorator
def sum_of_two(a,b):
  print("Inside the function")
  return a+b
a, b = 2, 3
print("Sum = ",sum_of_two(a,b))