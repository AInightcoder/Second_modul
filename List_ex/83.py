son = [2,5,8,95,41,65,58]

print(son)

x=len(son)
q=son[0]

son.remove(son[0])
son.insert(x-1,q)

print(son)