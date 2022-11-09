while(1):
    
    son= int(input("SON >>> "))

    a=int(son/100)
    b=int(son/10%10)
    c=int(son%10)

    value = c*100+a*10+b

    print(value)

   