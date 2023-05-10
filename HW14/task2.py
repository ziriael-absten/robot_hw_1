import re
# name = input("Enter file name: ")
name = "task2.txt"
lst = []
with open(name, "r") as f:
    for line in f:
        lst.append(line.split())
    # print(lst)
total_lst = []
for i in lst:
    line_ = ""
    for el in i:
        match = re.fullmatch(r"\b\S+@\w+\.(?:mail\.|gmai\.|email\.)?(?:com|net)\b", el)
        if match:
            line_ += "*@* "
        else:
            line_ += el + " "
    total_lst.append(line_)
# print(total_lst)
with open(name, "w") as f:
    for i in total_lst:
        f.write(f"{i}\n")


# renjvkreijk kjkjbrglkwe@email.com hj42gknj4
# rngof4w3kng@mail.net
# fj3ibnf j34gnfkj4@gmail.com


