a = [1,9,3,5,2,84,4,54,7,24,14]

for i in range(len(a)+1):
   if a[i-1]>a[i] and a[i]<a[i+1]:
      print(a[i]**2)
