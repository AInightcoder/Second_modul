while(1):
     # a< b
    a=int(input("A >>> "))
    b=int(input("B >>> "))

    counter=0

    for i in range(a,b+1):
        counter+=1
        print(i)
     
    print("Soni: ",counter)