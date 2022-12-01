son = [2,5,10,8,9,54,1,5,6,8,14,3,6,9]

ozlash=[]

for i in range(len(son)):

  if son[i-1]>son[i]:
    ozlash.append(son[i-1])

print(ozlash)    