with open("fifth.txt", "r") as fifth:
   satr= fifth.read()

with open("sexth.txt", "a+") as sexth:
    sexth.write(satr)
    sexth.write('\n')
