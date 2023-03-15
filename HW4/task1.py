msg = input("Enter some text ")
if msg.isdigit():
    print("It's a number ")
    if int(msg) % 2 == 0:
        print("This number is even ")
    else:
        print("This number is odd ")
elif msg.isalpha():
    print("It's a string ")
    print(f"There are {len(msg)} letters in this string ")
else:
    print("I don't know what data type it is ")