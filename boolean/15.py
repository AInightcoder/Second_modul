while (1):

    a = int(input("A >>> "))
    b = int(input("B >>> "))
    c = int(input("C >>> "))

    value = bool(a == b and a > c or b > c)

    print(value)
