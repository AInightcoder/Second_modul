satr = input("Enter: ")
satr2= input("Enter: ")

words=satr.split()
count=0

taker=''

for i in range(len(words)-1,0, -1):
    if count!=0:
       pass
    if words[i]==satr2:
       count+=1
       words[i]=''  
print(*words)




    

