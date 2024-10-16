#find out the execution time of a function using a decorator.
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
  def inner1(*args,**kwargs):
    start = time.time()
    func(*args,**kwargs)
    end = time.time()
    print("Total time taken in : ", func.__name__, end - start)
  return inner1

@calculate_time
def factorial(num):
  """sleep 2 seconds because it takes very less time so that you can see the actual difference"""
  time.sleep(2)
  print(math.factorial(num))

factorial(5)    