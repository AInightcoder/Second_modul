n = int(input("N >>> "))

JuftIn=[]
toqTesDe=[]
index=0

while index < n:


   if index%2==0:

      JuftIn.append(index)

   else:

      toqTesDe.append(index)
      toqTesDe.reverse() 

   index+=1     

print(JuftIn,toqTesDe)