
def identical(first_set, second_set):
    return first_set & second_set

def different(first_set, second_set):
    return first_set ^ second_set

def number(num):
    if num.isdigit():
        return True
    return False
numbers = ["1, 2, 4, 5, 7, 8, 6, 9", "8", "cat"]
filter_nums = filter(number, numbers)
result = list(filter_nums)
print(result)