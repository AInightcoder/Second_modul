import os, time
class MotivationSen:
   def __init__(self, firstw, secondw, thirdw, fourthw, fifthw, sexthw):
     self.firstw=firstw
     self.secondw=secondw
     self.thirdw=thirdw
     self.fourthw=fourthw
     self.fifthw=firstw
     self.sexthw=sexthw
   
   def birinchi(self):
      return self.firstw
   def ikkinchi(self):
      return self.secondw 
   def uchunchi(self):
      return self.thirdw
   def tortinchi(self):
       return self.fourthw
   def beshinchi(self):
       return self.fifthw  
   def oltinchi(self):
       return self.sexthw           

motivation=MotivationSen("Salom Hammaga !",
                        "O'z yo'lingni o'zing tanla !",
                        "Hayotda qaysi paytda qishnalishni bil ",
                        "Yoshlikda olingan bilm, Toshga o'yilgan naqish !",
                        "Hayotdagi o'zingni formulangni tuz !",
                        "Xayr sog'bo'ling !")
while 1:
  # clear = cls in terminal
  os.system('cls')       
  print(motivation.birinchi())  
  time.sleep(2) 
  os.system('cls')       
  print(motivation.ikkinchi())  
  time.sleep(2) 
  os.system('cls')       
  print(motivation.uchunchi())  
  time.sleep(2) 
  os.system('cls')       
  print(motivation.tortinchi())  
  time.sleep(2) 
  os.system('cls')       
  print(motivation.beshinchi())  
  time.sleep(2)
  os.system('cls')       
  print(motivation.oltinchi())  
  time.sleep(2)

    



  

