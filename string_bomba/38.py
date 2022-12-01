import re
s1=input("Enter_1: ")
s2=input("Enter_2: ")
s3=input("Enter_3: ")

son=s1.count(s2)

index = re.sub(s2," ",s1,count=son)
print(index)