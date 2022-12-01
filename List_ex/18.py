son=[7, 2, 3, 8, 5, 9, 10, 4]
a=len(son)
for i in range(len(son)):
  if son[i]<son[len(son)-1]:
     print(son[i])
     a+=1
     break
if a==len(son):
  print(0)    

  