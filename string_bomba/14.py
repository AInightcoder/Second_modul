while(1):
    satr=input("Enter teh satr... ")
    
    counter=0
    for i in range(len(satr)):
        if ord(satr[i])>=65 and ord(satr[i])<=90:
            counter+=1

    print("Katta harflar soni: ",counter)        