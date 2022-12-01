from math import pow

def Addrightdigit(R,K):

   son=str(K)
   yor_dam=len(son)
   onni_darajasi=pow(10,yor_dam)
   
   return R*onni_darajasi+K
R=1
while(R!=0):

    R=int(input("Enter: "))
    K=int(input("Enter: "))  

    print(Addrightdigit(R,K))