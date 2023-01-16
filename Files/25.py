with open('eleventh.txt', 'r') as f:
     counter=0
     new=[]
     k=2
     satr=f.readlines()
     for line in satr:
      for j in range(len(line[0])):
        if line[j]==" ":
          new=satr.remove(line)
          counter+=1
      print(counter,new) 

# it is bad....


     
    
   
         
                 
         
             