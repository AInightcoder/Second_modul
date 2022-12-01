n=int(input("N >>> "))
d=5
arfmetik_pro=[]
index=0

while index < n:
   arfmetik_pro.append((index-1)+d)
   index+=1
   
for i in range(len(arfmetik_pro)):  
    print([i],"=",arfmetik_pro[i])   