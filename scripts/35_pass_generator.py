import string
from random import randint

print("### PASS GENERATOR ###\n\n\n")

print("enter a length of your pass [default 16]: ")
length_answer = input()
LENGTH = 16 if not length_answer else int(length_answer)


password = []
for i in range(LENGTH):
    r = randint(0, len(string.printable))
    password.append(string.printable[r])

print("generated pass is:")
print("".join(password))



