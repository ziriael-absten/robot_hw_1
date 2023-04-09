new_dict = {}
while True:
    command = input("Enter a command: ")
    if command == "add":
        name = input("Enter a name: ")
        number = input("Enter a number: ")
        new_dict[name] = number
    elif command == "stats":
        print(len(new_dict))
    elif command == "delete <name>":
        del_name = input("Enter a name you want to delete: ")
        del new_dict[name]
    elif command == "list":
        print(new_dict)
    elif command == "show <name>":
        name = input("Enter a name: ")
        print(new_dict[name])