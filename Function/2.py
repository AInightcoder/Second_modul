from math import pow

def PowerA234(num):
    
  natija = pow(num,2),pow(num,3),pow(num,4)
  return natija

A=float(input("Enter the A num: ")) 
B=float(input("Enter the B num: "))
C=float(input("Enter the C num: "))

print(PowerA234(A))
print(PowerA234(B))
print(PowerA234(C))