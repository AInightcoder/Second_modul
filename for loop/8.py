while(1):
    a=int(input("A >>> "))
    b=int(input("B >>> "))
    value=1
    for i in range(a, b):
        value*=i
        
    print(value)