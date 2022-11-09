while(1):
    a=int(input("A >>> "))
    value=0
    for i in range(a):
        value+=pow((a+i),2)
        
    print(value)