# Advance_Python

que1- What is the difference between wrapper and decorator in Python?
ans-A wrapper is the inner function defined within a decorator that actually performs the added functionality.
A decorator is the outer function that takes a function as an argument, defines a wrapper function to modify ##it, and returns the wrapper.

Que2-What is function vs decorators in Python?
Ans- function:- function is a block of code that perform special task,accept inputs(argument),process and ##return output
decorators:- decorators is a higher order function that takes another function as argument, add some ##functionality and return new function(wrapper func),it allows modifications, changing behavior of original ##function which passed as argument.

Que-When should you use decorators in Python?
Ans-Decorators are used for changing behavior of original function..Use them when you want to add ##functionality like logging, caching, or authentication to existing functions without modifying their source ##code.
