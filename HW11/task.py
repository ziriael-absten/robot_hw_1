new_dict = {}
while True:
    command = input("Enter a command: ")
    if command == "add":
        name = input("Enter a name: ")
        number = input("Enter a number: ")
        new_dict[name] = number
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
