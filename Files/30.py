with open('eleventh.txt', 'r') as f:
  
   satr=f.read().split()
   max=max(satr, key=len)
   print(max)  
   
