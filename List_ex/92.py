son = [2,5,9,47,5,6,3,4,7,9]

print(son)

for i in range(len(son)-1):
  if son[i]%2!=0:
    del son[i]
print(son)    