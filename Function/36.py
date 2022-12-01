def Fib(N):

    son=0; son1=1; son2=2
    for i in range(3,N):
      son=son1+son2
      son1=son2
      son2=son
    print(son)


N=int(input("N >>> "))
Fib(N)