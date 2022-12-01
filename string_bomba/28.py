
satr=input("Enter a sentence: ")

c=input("belgi: ")

for i in range(len(satr)):
  if satr[i]==c:
     x=satr[:i]+"c"*2+satr[i:]   
     
print(x)


  
