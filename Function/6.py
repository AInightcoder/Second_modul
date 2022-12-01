def DigitCountSum(son):
  count=0
  sum=0

  while  son!=0:
     sum+=son%10
     count+=1
     son/10

  return count, sum  

a=int(input("Enter the A num: ")) 
b=int(input("Enter the B num: "))
c=int(input("Enter the C num: "))

print(DigitCountSum(a))
print(DigitCountSum(b))
print(DigitCountSum(c))