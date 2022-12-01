import statistics


def mean(son):
  
  son=[a,b,c,d]
  son1=(a*b*c*d)/4
  return statistics.mean(son), son1
  

a=int(input("Enter the A num: ")) 
b=int(input("Enter the B num: "))
c=int(input("Enter the C num: "))
d=int(input("Enter the D num: "))

print(mean(a)) 

