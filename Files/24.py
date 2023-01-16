with open('eleventh.txt', 'r') as f:
  
  counter=0
  
  satr=f.readlines()
  for line in satr:
    for j in range(len(line[0])):
      if line[0]==" ":
        counter+=1
        
  print(counter)      

     
    
 
     
    
   
         
                 
         
             