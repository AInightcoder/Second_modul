son=[2, 8, 5, 78, 95, 6 , 3, 45]

count=0
for i in range(len(son)):
  if son[i-1]<son[i]:
    print([i])
    count+=1
print(count)    