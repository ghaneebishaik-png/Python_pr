##Decorators::Decorator is a function that modifys/enhance the current function without changing its actual code. Decorator adds extra functionality of a function.
def deco(func):
    def func2():
        print("before func")
        func()
        print("After func")
        func()
    return func2
@ deco
def func1():
    print("Decorator func")

func1()


##Decorator function to calculate time taken by original function

from datetime import datetime

import time

def decorator(function):
    def function2():
        start_time = datetime.now()
        print(start_time)
        function()
        end_time = datetime.now()
        print(end_time)
        print(f"Time taken by a function {end_time - start_time}")
    return function2

@decorator
def function1():
    for i in range(10):
        print(i)
        time.sleep(0)
function1()


##Generator is special type of functions that returns values one by one. Uses yield instead of return. Doesn't store all values in memory, best for large data optimization.

def fun1():
    for i in range(31):
        yield i
t1 = fun1()
print(t1)
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))