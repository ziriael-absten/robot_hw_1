class MyStr():
    def __init__(self, str):
        self.str = str.upper()

    def __str__(self):
        return self.str

# my_str = MyStr('test')
#
# print(my_str)