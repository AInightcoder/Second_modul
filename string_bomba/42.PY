satr = input("Enter: ")

words = satr.split()
print(words)
count=0
for i in words:
     if i[0]==i[::-1][0]:
          count+=1
print(count)          


