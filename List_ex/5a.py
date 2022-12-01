n = int(input("N >>> "))

fibonachchi=[]
index=0
F=0; F1=1; F2=2
for i in range(n-2):
  fibonachchi.append(F)
  F=F1+F2 
  F1=F2
  F2=F


for i in range(len(fibonachchi)):
   print(fibonachchi[i])

   
