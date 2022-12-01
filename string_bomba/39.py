satr = input("Enter: ")

words = satr.split()
print(words)

p1=int(input("Enter_p1: "))
p2=int(input("Enter_p2: "))

print(*words[p1:p2])
