while(1):   
    char = input("Enter the satr..")
    sonlar=0; nuqtalar=0; 

    for i in range(len(char)):
        
        if ord(char[i])>=48 and ord(char[i])<58:
                sonlar+=1
        elif ord(char[i])==46: 
            nuqtalar+=1
        

    print(sonlar,nuqtalar)

    if sonlar>=1 and nuqtalar==0:
        print("Natija: 1\n")
    elif sonlar>=1 and nuqtalar==1:
        print("Natija: 2\n")
    else:
        print("Natija: 0")
