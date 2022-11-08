while (1):
    x = int(input("X >>> "))
    x1 = int(input("X1 >>> "))
    x2 = int(input("X2 >>> "))
    y = int(input("Y >>> "))
    y1 = int(input("Y1 >>> "))
    y2 = int(input("Y2 >>> "))
    # x<3 and X>-3 and y<3 and y>-3
    
    value = bool(x1 > -3 and y1 > 3 and x <
                 x1 and y < y1 and x2 > 3 and y2 > -3)

    print(value)
   