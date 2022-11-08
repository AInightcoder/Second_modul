while(1):

    A=float(input("A >>> "))
    B=float(input("B >>> "))
    C=float(input("C >>> "))

    if abs(A-B)>abs(A-C):
        print("C nuqta yaqin: ",abs(A-C))
    else:
        print("B nuqta yaqin ",abs(A-C))    