class User:
    def __init__(self, name):
        self.name = name.lower()

    def __eq__(self, other):
        return self.name == other.name

# first_user = User('OLEKSII')
#
# second_user = User('Oleksii')
#
# print(first_user == second_user)
