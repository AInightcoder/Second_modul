def Prime(N):

  for i in range(2,N):
    if N%i==0:
      print(False)
      break
  else:
      print(True)
  

son=int(input("Son >>> "))
Prime(son)
