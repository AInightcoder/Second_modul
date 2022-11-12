while(1):

    satr=input("Enter the satr .... ")

    counter=0
    counter2=0

    for i in range(len(satr)):
        if ord(satr[i])>=97 and ord(satr[i])<=122:
            counter+=1
        if ord(satr[i])>=192 and ord(satr[i])<=225:
               counter2+=1    
        sum=counter2+counter
    print("Kiril va kichik lotin harflar soni: ",sum)        