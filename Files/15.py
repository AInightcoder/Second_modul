import re
k=int(input("K >>> "))
with open('eleventh.txt', 'r') as f:
  lines = f.readlines()
  lines.pop(k)        
with open('eleventh.txt', 'w') as f:
    f.writelines(lines)    
         
             
           
     

 
       
   
     
        

    
         

                 
