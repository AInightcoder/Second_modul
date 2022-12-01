from math import pow

def Triangle(son):
  area=(son*son)*1.73/4
  return area

a=float(input("Enter the A num: ")) 
b=float(input("Enter the B num: "))
c=float(input("Enter the C num: "))

print(Triangle(a))
print(Triangle(b))
print(Triangle(c))