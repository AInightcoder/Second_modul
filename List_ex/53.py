a = [2,4,5,7,9,88]
b = [4,8,9,65,24,5]

c=[]

for i in range(len(a)):
  c.append(max(a[i],b[i]))

print(a,b,c, sep="\n")
