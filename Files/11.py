with open("eleventh.txt","r") as eleventh:
    satr=eleventh.readlines()
    son=0
    for i in satr:
      if "\n" in satr:
        son=satr[i].index("\n")
        satr.insert(son,"\n")
      break 
with open("eleventh.txt","w") as eleventh:        
    eleventh.writelines(satr)