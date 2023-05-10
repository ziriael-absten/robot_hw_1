import re

phone_number_pattern = r'^(\+?3?8?)?0\d{9}$'
phone_number_regex = re.compile(phone_number_pattern)

new_dict = {}

while True:
    command = input("Enter a command: ")
    if command == "add":
        name = input("Enter a name: ")
        number = input("Enter a number: ")
        match = re.fullmatch(r'^(\+?3?8?)?0\d{9}$', number)
        if match:
            new_dict[name] = number
            print("Number added successfully!")
        else:
            print("Invalid phone number format!")
    elif command == "stats":
        print(len(new_dict))
    elif command == "delete":
        del_name = input("Enter a name you want to delete: ")
        try:
            del new_dict[del_name]
        except KeyError:
            print("This person is not in the phone book!")
    elif command == "list":
        print(new_dict)
    elif command == "show":
        name = input("Enter a name: ")
        try:
            print(new_dict[name])
        except KeyError:
            print("This person is not in the phone book!")