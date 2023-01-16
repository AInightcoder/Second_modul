son = [5,9,6,15,78,3,6,1,5]

max=0
min=son[0]

k=5

for i in range(len(son)):
   if son[i]>max:
      max=son[i]
      son.insert(i,k)
print(max)      
