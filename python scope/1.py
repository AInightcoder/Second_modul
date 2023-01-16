"""
Python scope --> bu recursiya o'xshash bo'lib ... funcsiya ichida boshqa funksiya qo'llash hisoblandi..

ular two xil bo'ladi: local va global

local>> funcsiya ichidagi o'zgaruvchi
golobal>> funcsiya tashqarisidagi

keyword = global ____

"""

global x
x = 400

def local():
  print(x) # o'zgaruvchi global bo'lgani uchun chiqamydi

def globald():
   global x
   x=1000
   

print(x)


