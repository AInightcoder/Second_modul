while(1):

    n=int(input("Enter the NUM..."))
    satr=input("Enter: ")

    value=len(satr)

    if n==value:
        print(satr)

    elif n<value:
        print(satr[:n])

    elif n>value:
        s= n-value
        result = s*'*'+satr
        print(result)
