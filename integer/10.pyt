while(1):
    
    son= int(input("SON >>> "))

    a=int(son/100)
    b=int(son/10%10)
    c=int(son%10)

    value = b*100+c*10+a

    print(value)

   