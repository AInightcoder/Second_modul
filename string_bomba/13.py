while(1):
    satr=input("Enrter the satr... ")

    counter=0

    for i in range(len(satr)):
        if ord(satr[i])>=48 and ord(satr[i])<=57:
            counter+=1

    print(counter)        