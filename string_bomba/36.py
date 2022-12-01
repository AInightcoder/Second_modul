import re
s1=input("Enter_1: ")
s2=input("Enter_2: ")
s3=input("Enter_3: ")

index = re.sub(s2,s3,s1,count=1)
print(index)