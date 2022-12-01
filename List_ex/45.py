
son = [2,4,8,9,14,5,67,25,18,11]

ayirma = abs(son[0]-son[1]); a=1

for i in range(len(son)):
  if abs(son[i-1]-son[i]<ayirma):
      ayirma=abs(son[i-1]-son[i])
      a=i

print(son[a],"and",son[a-1])      