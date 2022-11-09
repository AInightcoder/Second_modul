while(1):
    a=int(input("A >>> "))
    b=int(input("B >>> "))
    value=0
    for i in range(a, b):
        value+=pow(i,2)
        
    print(value)