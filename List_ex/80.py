a = [1,9,3,5,2,84,4,54,7,24,14]

x=len(a)
q=a[x-1]

a.remove(a[x-1])
a.insert(0, q)
print(a)