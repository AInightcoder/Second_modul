while(1):
    
    son=int(input("SON >>> "))
    son1=int(input("SON1 >>> "))
    son2=int(input("SON2 >>> "))
    
    count=0; count1=0

    if   son>0:
         count+=1
    else:
        count1+=1
    if son1 > 0:
         count+=1
    else:
        count1+=1     
    if son2 > 0:
         count+=1
    else:
        count1+=1     
 
    print("Musbatlar_soni:",count)
    print("Manfilarlar_soni:",count1)
    