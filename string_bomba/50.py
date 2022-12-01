import re
satr = input("Enter: ")
result=''

result=re.sub(r"\s{2,}"," ",satr)
 
print(result)
