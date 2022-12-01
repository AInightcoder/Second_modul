import re

satr = input("Enter: ")

words = re.sub(" ",".",satr)

print(words)
