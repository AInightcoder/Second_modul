while(1):
    A=float(input("A >>> "))
    B=float(input("B >>> "))
    help

    if A > B:
        help=A
        A=B
        B=help
        print("B=",B)
        print("A=",A)
    else:
        print("B=",B)
        print("A=",A)

