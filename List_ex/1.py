N=int(input("N >>> "))

toq_son_massive=[]
index=1

while index < N*2:
    if index%2!=0:
        toq_son_massive.append(index)
    index+=1
print(toq_son_massive)
