while(1):
     # a< b
    a=int(input("A >>> "))
    b=int(input("B >>> "))

    counter=0

    for i in range(b-1, a, -1):
        print(i)
        counter+=1
     
    print("Soni: ",counter)