import re

satr=input("Enter: ")

word = satr.upper().split()
space = word.sort()
space=re.sub(r"s\{2,}"," ",satr)
print(space)