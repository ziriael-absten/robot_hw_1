# first solution
def first_sol(lst):
    return max(lst)

# second solution
def second_sol(lst):
    the_biggest_num = lst[0]
    for i in lst:
        if i > the_biggest_num:
            the_biggest_num = i
    return the_biggest_num

# third solution
x = lambda lst: max(lst)




