import json
import datetime
try:
    with open("phonebook.json", "r") as f:
        phonebook = json.load(f)
except FileNotFoundError:
    phonebook = {}

while True:
    command = input("Enter a command: ")
    if command == "add":
        name = input("Enter a name: ")
        number = input("Enter a number: ")
        phonebook[name] = number
        with open("phonebook.json", "w") as f:
            json.dump(phonebook, f)
    elif command == "stats":
        print(len(phonebook))
    elif command == "delete":
        del_name = input("Enter a name you want to delete: ")
        if del_name in phonebook:
            del phonebook[del_name]
            with open("phonebook.json", "w") as f:
                json.dump(phonebook, f)
        else:
            print("Name not found in phonebook.")
    elif command == "list":
        print(phonebook)
    elif command == "show":
        name = input("Enter a name: ")
        try:
            print(phonebook[name])
        except KeyError:
            print("This person is not in the phone book!")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("phonebook.json", "a") as f:
                f.write(f"KeyError was called at {timestamp}")

