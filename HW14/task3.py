import re
name = input("Enter file name ")
# name = "task3.txt"
lst = []
with open(name, "r") as f:
    for line in f:
        lst.append(line.split())
total_lst = []
for i in lst:
    line_ = ""
    for el in i:
        match = re.fullmatch(r"\b\S+@\w+\.(?:mail\.|gmai\.|email\.)?(?:com|net)\b", el)
        if match:
            word = f"{el[0]}***@****{el[len(el)-1]}"
            line += f"{word} "
        else:
            line += f"{el} "
    total_lst.append(line)
# print(total_lst)
with open(name, "w") as f:
    for i in total_lst:
        f.write(f"{i}\n")
