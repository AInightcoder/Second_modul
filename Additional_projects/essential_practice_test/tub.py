son=int(input("Enter: "))

count=0

for i in range(2,10**10):
  for j in range(2,10**10):
    if i%j==0 and i!=j:
       print(False)
       break
    if i%j==0 and i==j:
       count+=1
       print(True)
       break  
  if count==son:
    break

