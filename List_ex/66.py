a = [1,5,8,5,84,54,24,14]
firstevennum=0

for i in range(len(a)):
  if a[i]%2==0:
     firstevennum=a[i]
     break

for i in range(len(a)):
    a[i]=a[i]+firstevennum
print(a)    