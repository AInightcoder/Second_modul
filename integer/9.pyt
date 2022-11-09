while(1):
    
    son= int(input("SON >>> "))

    a=int(son/100)
    b=int(son/10%10)
    c=int(son%10)

    value = a*100+c*10+b

    print(value)

   