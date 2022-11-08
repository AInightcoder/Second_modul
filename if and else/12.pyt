while(1):
    A=float(input("A >>> "))
    B=float(input("B >>> "))
    C=float(input("C >>> "))
    D=float(input("D >>> "))

    if A==B==C:
        print(4)
    if A==B==D:
        print(3)    
    if B==C==D:
        print(1)
    if A==C==D:
        print(2)  
    


