input = input("Enter the satr... ")
result =""

for char in input:
    
      if ord(char)>= 97 and ord(char)<= 122:
        result += char.upper()
    
      elif ord(char)>= 65 and ord(char)<= 90:
        result += char.lower()
    
print(result)

