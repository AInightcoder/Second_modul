class mall:
  # o'zgaruvchilar
  area =  "Bozorning kengligi: 100 X 500"
  color = "Devor ranglari: mix (blue, red, black, yellow and white)"
  store = "Do'konlar soni: 600"
  grocery_store = " kartoshka, piyoz, tomato, meat, shirinliklar, fruites"
  cloth_store = "shirt, shoes, jacket, T-shirt, naski"
  technology_store = "television, CD-player, kalonka, Phone, cooker, electrone_oven"
  car_store = "Malibu, Cobelt, Nexi_3, Matiz_best, Epka_est"
  # Client suhbati
  def client(self, tolking): 
      if tolking==1:
        print("Cliet keldi...")
        print("Admin bilan suhbat qilyapti...")
        print("Talking....")
        print("Talking....")
        print("Talking....")
        print("Client o'z savoliga javob oldi.")
        print("Suhbat yakunlandi.")
      else:
        print("Client tashqarida...")
        print("Ichkariga kirmadi va uyiga ketdi...")
  # Clienttda qidirish processi      
  def searchingProdact(self):
        print("Client Grocery storeda.")
        print(" Barcha mevalardan 2kgdan oldi. ")
        print("4kg gosht va 2kg sabzi ham oldi yana")
        print("Manimcha kechka osh bo'lsa kerak.")
   # Kyim tanlash       
  def clothing(self):
        print(self.cloth_store)
        print("Sotuvchi yuqoridagi narsalar haqida kilentga ma'lumot berdi.")
        print("Client butun oyoq-bosh kyim xarid qildi.")
        print("Umumiy xarajat $100 bo'ldi...")
   # Mashina tanlash     
  def cars(self, one):
        print(self.car_store)
        if one==1:
           print("Client Malibu tanladi.")
           print("Uning narxi $40000.")
           print("Mashina sotildi.")
        else:
          print("Mashinalarni baxti ochilmadi.")
          print("Mashina_bozor ishlamayopti, qor yog'gan.")
  def data(self):
          print("Savdo majmuasi haqida ma'lumot.")
          print(self.area)
          print(self.color)
          print(self.store)

dokon=mall()
while(1):
  print("Grocery: 1.     Car: 2.      Kiyim: 3.  ")
  son=int(input("Option tanlang: "))

  if son==1:  
    dokon.client(tolking=1)
    dokon.searchingProdact()
    dokon.data()
    print("\n")
  if son==2:
    dokon.client(tolking=1)
    dokon.clothing() 
    dokon.data()
    print("\n")
  if son==3:
    dokon.client(tolking=0)
    dokon.cars(one=0) 
    dokon.data()
    print("\n")


      
        
            
        



       

