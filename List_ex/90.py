son = [2,7,9,14,24,71,65,45]
k=5
for i in range(len(son)-1):
  if son[i]==son[k]:
    son.remove(son[i])
print(son)

# second method
son.pop(k)
print(son)