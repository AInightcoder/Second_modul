n = int(input("N >>> "))

firstNum=[]
secondNum=[]
index=0

while index < n:

  if index%2==0:
    firstNum.append(index)
    firstNum.append(index+1)
  else:
    secondNum.append(n-index-1)
    secondNum.append(n-index-2)   
  index+=1

print(firstNum+secondNum)