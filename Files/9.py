k=int(input("K >>> "))    

with open("ninth.txt","r") as ninth:
    satr=ninth.readlines()
    for i in satr:
      if satr.index(i)==k:
         satr.insert(k,"\n")

with open("ninth.txt","w") as ninth:        
  ninth.writelines(satr)