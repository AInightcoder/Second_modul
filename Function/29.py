def digitcount(K):
    count=0
    raqam=0
    son1=0
    while( K!=0):
      raqam=K%10
      count+=1
      K=K//10
    print(count)  
son=int(input("son >>> "))
digitcount(son)      

    
