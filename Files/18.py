with open('eleventh.txt', 'r+') as f:
  lines = f.readlines() 

with open('eleventh.txt', 'w') as f:
    f.writelines(" ")    
         
with open('eleventh.txt', 'w') as f:
     for char in lines:
        f.writelines(char[5:]) 
             
           
     

 
       
   
     
        

    
         

                 
