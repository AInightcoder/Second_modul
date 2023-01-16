class Iterator:
  def __iter__(self):
    self.num=1
    return self

  def __next__(self):

    res = self.num
    self.num+=1
    return res


entnum= Iterator()
myiter=iter(entnum)

print(next(myiter))
print(next(myiter))

