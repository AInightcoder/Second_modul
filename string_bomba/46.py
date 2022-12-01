satr = input("Enter: ")

word = satr.split()

max = 0
max_word=''

for lword in word:
  if len(lword) > max:
    max = len(lword)
    max_word = lword

print("The longest: ", max_word, "Length: ", max)    