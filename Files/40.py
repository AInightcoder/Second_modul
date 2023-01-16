with open('40a.txt', "r") as a:
  det=a.read()
 
  new=[]
  counter=0
  while len(det)>0:
    if counter==30:
         new.append(det[:counter]) 
    counter+=1
    
  print(new)  
    

# with open('40b.txt', "r") as b: 
#   det2=b.read().split()
#   print(det2)

