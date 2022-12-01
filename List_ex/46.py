son = [1,5,9,45,68,74,6,12,14]
a=1
R=10
for i in range(len(son)):
  if( son[i-1]+son[i]<R):
     a=i
print(son[a-1],"and",son[a])     
