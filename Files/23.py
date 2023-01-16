with open('eleventh.txt', 'r') as f:
     new=[]
     k=4
     satr=f.readlines()
     counter=0
     for i in satr:
      counter+=1
     new=satr[counter-k:]
     print(*new)
with open('eleventh.txt', 'w') as f:    
     f.writelines(new) 
     
    
   
         
                 
         
             