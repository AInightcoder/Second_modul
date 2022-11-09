while(1):
    a=int(input("A >>> "))
   
    value=1
    for i in range(1,a):
        value*=1+(i/10)
        
    print(value)