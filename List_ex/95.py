son = [2,5,9,9,47,5,5,6,3,3,4,7,9]
list=[]
for i in range(len(son)):
  if son[i-1]!=son[i]:
     list.append(son[i])
print(list)