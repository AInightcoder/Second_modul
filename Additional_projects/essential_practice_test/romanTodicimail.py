def romanToInt(sim):

   sum = 0
   one_time_skip = False
   for i in sim:
        if one_time_skip:
            one_time_skip = False
            continue
        if i == "I":
            if sim[sim.index(i)+1]=="V":
                one_time_skip = True
                sum = sum + 4
            elif sim[sim.index(i)+1]=="X":
                one_time_skip = True
                sum = sum + 9
            else:
                sum = sum + 1
        elif i == "V":
            sum = sum + 5

        elif i == "X":
            sum = sum + 10

        elif i == "L":
            sum = sum + 50

        elif i == "C":
            sum = sum + 100

        elif i == "D":
            sum = sum + 500

        elif i == "M":
            sum = sum + 1000
   return sum

s = input("S: ")
print(romanToInt(s))