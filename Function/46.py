from math import gcd
 
def EKUB(A,B):
  return gcd(A,B)

son1 = int(input("Son1 >>> "))
son2 = int(input("Son2 >>> "))

print(EKUB(son1,son2))
