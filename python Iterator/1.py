mytupl=('salom', 'hammaga', 'qanday')

modifier = iter(mytupl)

for i in range(len(mytupl)):
  print(next(modifier))