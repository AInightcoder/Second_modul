son=[7, 16, 3, 8, 5, 9, 10, 15]
minJuft=[]
minimum=0
for i in son:
  if i%2==0:
    minJuft.append(i)
    #print(minJuft)
    minimum=min(minJuft)
print(minimum) 
 
   
