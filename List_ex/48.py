son = [1,4,5,8,95,9,34,6,6,5,8,4,2,1,63,58,41]

ozlash=[]

for i in range(len(son)):
  for j in range(i+1,len(son)):
    if son[i]==son[j]:
      ozlash.append(son[i])

print(ozlash)
