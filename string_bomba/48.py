# import re
# satr = input("Enter: ")

# words = satr.split()
# status=''

# for i in words:
  
#   if words[0]==words[i]:
#       status = re.sub(words[i],".")

# print(status)




satr = "dyunyoy syeydnyi tog'angdmas"
satr2="topdimsani"

belgilar = []
for i in satr:
    if i=="a":
        belgilar.append(satr2)
    else:
       belgilar.append(i)    

print(belgilar)

belgilar2 = [i*2 if i!="a" else "a harfi bor i" for i in satr ]

print(belgilar2)
# print(len([i for i in satr.split() if i.count("y")>2]))