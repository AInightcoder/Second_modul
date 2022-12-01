a = [2,4,5,7,9,88]
b = []

for i in range(len(a)):
  if a[i] < 5:
    b.append(2*a[i])
  else:
    b.append(a[i]/2)  

print(a, end="\n")
print(b)