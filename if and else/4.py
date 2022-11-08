while(1):

    son=int(input("SON >>> "))
    son1=int(input("SON1 >>> "))
    son2=int(input("SON2 >>> "))
    
    count=0

    if   son>0:
         count+=1
    if son1 > 0:
         count+=1
    if son2 > 0:
         count+=1
 
    print(count)