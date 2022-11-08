while(1):
    A=float(input("A >>> "))
    B=float(input("B >>> "))
    C=float(input("C >>> "))


    if A > B and B > C:
        print(C,A)
    if A > C and  C > B:
        print(B, A)    
    if B > A and A > C:
        print(C , B)
    if B > C  and C > A:
          print(A, B)  
    if C > A and A > B:
        print(B , C)     
    if C > B and B > A:
        print(A, C)


