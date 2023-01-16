import re

with open('eleventh.txt', 'r') as f:
  lines = f.readlines()
  counter=0
  for i in lines:
       counter+=1
  lines.pop(counter-1)        
with open('eleventh.txt', 'w') as f:
    f.writelines(lines)    
         
             
           
     

 
       
   
     
        

    
         

                 
