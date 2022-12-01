son=[2, 8, 5, 78, 95, 6 , 3, 45]

for i in range(len(son)):
  if son[i-1]>son[i] and son[i+1]>son[i]:
    print([i])
       