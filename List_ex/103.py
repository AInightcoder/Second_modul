son = [5,9,6,52,3,65,7,6,55]
k=4
max=0
min=son[0]
for i in range(len(son)):
  if son[i]>max:
    max=son[i]
    son.insert(i+2,k)
  if son[i]<min:
    min=son[i]
    son.insert(i,k)   
print(son) 
