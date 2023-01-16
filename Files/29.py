with open('eleventh.txt', 'r') as f:
   max=''

   for i in f.read().split(" "):
      if len(i)>len(max):
        max=i
   print(max)   

