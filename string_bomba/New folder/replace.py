# we can replace " " with " "

a="Salom hammag"

for i in range(len(a)):
  if a[i]=='l':
    txt=a.replace(a[i],"d")

print(txt)