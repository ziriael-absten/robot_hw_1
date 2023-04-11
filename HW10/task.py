def to_zero(num):
    if num > 0:
        num -= 1
        print(num)
    to_zero(num)


# task2
def fibonacci(n: int):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# task3
def factorial(n: int):
    if n < 2:
        return 1
    return n * factorial(n - 1)

print(factorial(5))