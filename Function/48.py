from math import lcm
def EKUK(A,B):
  return lcm(A,B)

son1 = int(input("Son1 >>> "))
son2 = int(input("Son2 >>> "))
son3 = int(input("Son3 >>> "))

print(EKUK(son1,son2))