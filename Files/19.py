with open('eleventh.txt', 'r') as f:
     
     satr=f.read()
     saon= satr.swapcase()
with open('eleventh.txt', 'w') as f:
     f.write(saon)    
         
             