# maktab o'qituvchilari haqida ma'lumot (location , and phone number)
# oylik miqdori
# kunlik xarajati
# ishlash vaqti (berilgan fanlariga bog'liq)

class Teacher:
   def __init__(self, lname, fname, age, gender, phnumber,
                                    location, salary, day_xarajat, work_time):
    self.lname=lname
    self.fname=fname
    self.age=age
    self.gender=gender
    self.phnumber=phnumber
    self.location=location
    self.salary=salary
    self.day_xarajat=day_xarajat
    self.work_time=work_time

   def familya(self):
    return (self.lname)
   def ism(self):
    return (self.fname)
   def yoshi(self): 
    return (self.age)
   def jins(self):
    return (self.gender)
   def tel_number(self):  
    return (self.phnumber)
   def manzili(self): 
    return (self.location)
   def oylik(self):
    return (self.salary) 
   def xarajat(self):
    return (self.day_xarajat)
   def ishvaqti(self):
    return (self.work_time) 
  
lname=input("Enter the last name of taecher: ")
fname=input("Enter the first name of taecher: ")
age=input("Enter the age of taecher: ")
gender=input("Enter the gender of taecher: ")
phnumber=input("Enter the phnumber of taecher: ")
location=input("Enter the location of taecher: ")
oylik=input("Enter the Salary of teacher: ")
xarajat=input("Enter the expenses of teacher: ")
ishvaqti=input("Enter the work_time of teacher: ")

teacher1=Teacher(lname,fname,age,gender,phnumber,location,
                                                 oylik,xarajat,ishvaqti)  

print("===========================================")

print("LastName: ",teacher1.familya())
print("FirstName: ",teacher1.ism())
print("Age: ",teacher1.yoshi())
print("Gender: ",teacher1.jins())
print("Phnumber: ",teacher1.tel_number())
print("Location: ",teacher1.manzili())
print("Salary: ", teacher1.oylik())
print("Expenses: ",teacher1.xarajat())
print("Work_time: ", teacher1.ishvaqti())

print("===========================================")        

     



