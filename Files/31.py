with open('eleventh.txt', 'r') as f:
   k=5
   met=[]
   set1=''
   satr=f.read().split()
   for line in satr:
     if len(line)==k:
       met.append(line)
       
with open('eleventh.txt', 'w') as f:
  f.writelines(str(met))

  
    
   
