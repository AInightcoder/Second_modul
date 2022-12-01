a = [2,4,5,7,9,88,4,8,9,65,24,5]
b = []

for i in range(len(a)):
  if a[i]%2==0:
    b.append(a[i])
print(a,b, sep='\n')    
