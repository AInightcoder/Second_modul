#stopiterator

class Iterator:
  def __iter__(self):
    self.num = 1
    return self

  def __next__(self):
    if self.num < 20:
      x = self.num
      self.num +=1
      return x
    else:
      raise StopIteration


myiter=Iterator()
new=iter(myiter)

for x in new:
  print(x)
   