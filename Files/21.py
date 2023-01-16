with open('eleventh.txt', 'r') as f:
     new=[]
     satr=f.readlines()
     print(*satr)
     satr.reverse()
     new2=satr[3:]
     print("===============================")
     new2.reverse()
     print(*new2)
     
    
with open('eleventh.txt', 'w') as f:
       f.writelines(new2)    
         
                 
         
             