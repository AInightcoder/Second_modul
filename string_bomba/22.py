while(1):

    satr=input("Enter the satr... ")
    
    sum=0
    for i in range(len(satr)):
        sum+=ord(satr[i])
    print("Natija: ", sum)    