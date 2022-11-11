while(1):
    belgi=input("Enter the Char: ")
    
    char=str(ord(belgi))
    
    if int(char)>=65 and int(char)<=90 or int(char)>=97 and int(char)<=122:
       print("lotin")
    elif int(char)>=48 and int(char)<=57:
        print("digit")
    else:
        print(0)     
    
        