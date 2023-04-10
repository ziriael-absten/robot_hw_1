msg = input("Enter some text: ")
for i in msg:
    if i.isdigit():
        print("This is a number ")
        if int(i) % 2 == 0:
            print("This number is even")
        else:
            print("This number is odd")
    elif i.isalpha():
        print("This is a letter")
        if i.islower():
            print("This letter is lowercase")
        else:
            print("This letter is uppercase")
    else:
        print("This is a symbol")