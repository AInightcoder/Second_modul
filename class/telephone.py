class Telefon:
         rangi = "Blue"  #  bu rangi uchun o'zgaruvchi
         model = "Redmi 9 C pro max"
         xotira = "128 GB"
         camera_soni = "4 ta"
         yadrosi = "245 psp"

   # self bu yerda class ichida functionlarni chaqirish uchun isshlatiladi.!

         def call(self, gudok):
             print('Telphone qilinmoqda...')
             print('gudok...')
             print('gudok...')
             print('Telphone yakunlandi...')
         def switchonFlashlight(self, yondi):
             if yondi==1:
                print("it is working")
             else:
                print("it isn't working")

         def rasmga_olish(self, holati):
             if holati==1:
                print("Rasmga olish muaffiqiyatli amalga oshirildi")
             else:
                print("Rasmga olish muaffiqiyatli amalga oshirilmadi")

telephone1 = Telefon()
telephone1.call("+998939033301")
telephone1.rasmga_olish(holati=1)
telephone1.switchonFlashlight(yondi=1)
telephone1.rasmga_olish(holati=0)
telephone1.switchonFlashlight(yondi=0)

# class yakunlandi, yani obyekt tugadi.
    
                            