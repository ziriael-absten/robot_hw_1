import datetime


def log_function_call(func):

    def wrapper():
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("function_calls.log", "a") as f:
            f.write(f"{func.__name__} called at {timestamp}\n")

    return wrapper

@log_function_call
def sayhallo():
    print("Hello world! ")

sayhallo()