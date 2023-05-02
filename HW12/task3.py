import time
def name_time(times):
    def decor(func):
        def inner():
            for i in range(times):
                print(f"Function {func.__name__} called at {time.strftime('%H:%M:%S', time.localtime())}")
                func()
        return inner
    return decor

@name_time(3)
def my_function():
    print("Hello, world!")

my_function()