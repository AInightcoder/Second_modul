n=int(input("N >>> "))
with open("second.txt", "w") as second:
   for i in range(n):
     for j in range(97,97+i):
       second.write(chr(j))
     second.write('\n')  