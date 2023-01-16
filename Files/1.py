n=int(input("N >>>"))
k=int(input("K >>>"))
with open("first.txt","a+") as first:
  for i in range(n):
    for j in range(k):
      first.write("*")
    first.write("\n")