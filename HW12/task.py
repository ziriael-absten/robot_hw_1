import datetime
import time
def name_time(func):
    def inner():
        print(f"Function {func.__name__} called at {time.strftime('%H:%M:%S', time.localtime())}")
        func()
    return inner

@name_time
def my_function():
    print("Hello, world!")

my_function()