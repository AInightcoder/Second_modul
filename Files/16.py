with open('eleventh.txt', 'r') as f:
  lines = f.readlines() 
  counter=0
  for count in lines:
    if count.strip()=="":
      counter+=1
  print(counter)    

  for i in range(len(lines)-counter):
    if lines[i].strip()=="":
       lines.remove(lines[i])     
     
with open('eleventh.txt', 'w') as f:
    f.writelines(lines)    
         
             
           
     

 
       
   
     
        

    
         

                 
