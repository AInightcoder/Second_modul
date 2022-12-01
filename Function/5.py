def RectPS(x1,x2,y1,y2):

  P=abs(x1-x2)+abs(y1-y2)
  S=abs(x1-x2)*abs(y1-y2)

  return P, S

x1=int(input("Enter the x1 num: ")) 
x2=int(input("Enter the x2 num: "))
y1=int(input("Enter the y1 num: "))
y2=int(input("Enter the y2 num: "))

print(RectPS(x1,x2,y1,y2))