from itertools import permutations

s1=input("Enter_1: ")

word=[x.lower() for x in s1]

for y in list(permutations(word)):
  print("".join(y))



