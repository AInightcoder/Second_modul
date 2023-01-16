import re

with open('eleventh.txt', 'r') as f:
    lines = f.readlines()
    satr='salom men seni topdim'
    for i in lines:
       if  i.strip()=="":
        son=lines.index(i)
    lines.insert(son,satr) 

with open('eleventh.txt', 'w') as f:    
  f.writelines(lines)  
       
   
     
        

    
         

                 
