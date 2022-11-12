while(1):
    satr=input("\n\nEnetr the satr... ")
    n=int(input("N >>> "))

    beldi='*'
    for i in range(len(satr)):
        print(satr[i], end=" ")
        for j in range(n):
            print(beldi, end=" ")

