import sqlite3

class Oqituvchi:

  def __init__(self, database) -> None:
     self.conn=sqlite3.connect(f'{database}.db')

  def create_table(self, ):
    print("Table tashkil topyapti. ")
    self.conn.execute("""CREATE TABLE TEACHERS (ID INT NOT NULL PRIMARY KEY,
                            FNAME        STR   NOT NULL,
                            LNAME        STR   NOT NULL, 
                            AGE          INT,
                            BORN_YEAR    INT,
                            EXPERIENCE   STR,
                            FAMILY_CASE  STR,
                            WORK_TIME    STR,
                            SUBJECT      STR );""")
    
    print("Table yakunlandi.") 

  def add_person(self, ID: int, FNAME: str,LNAME: str,AGE: int,BORN_YEAR: int,EXPERIENCE: str,FAMILY_CASE: str,WORK_TIME: str,SUBJECT: str) -> None:

    print("Shaxs tablega qo'shish boshlandi...")
    
    firstStep="INSERT INTO TEACHERS (ID,FNAME,LNAME,AGE,BORN_YEAR,EXPERIENCE,FAMILY_CASE,WORK_TIME,SUBJECT)  VALUES"
    secondStep=f"({ID},'{FNAME}','{LNAME}',{AGE},{BORN_YEAR}, '{EXPERIENCE}','{FAMILY_CASE}','{WORK_TIME}', '{SUBJECT}');"
    sumAll=firstStep+secondStep
    self.conn.execute(sumAll)
    self.conn.commit()

    print("Tablega shaxs qo'shildi.")


  def show_person(self, ID, FNAME, LNAME, AGE, BORN_YEAR, EXPERIENCE, FAMILY_CASE, WORK_TIME, SUBJECT):
    
    self.ID=ID
    self.FNAME=FNAME
    self.LNAME=LNAME
    self.AGE=AGE
    self.BORN_YEAR=BORN_YEAR
    self.EXPERIENCE=EXPERIENCE
    self.FAMILY_CASE=FAMILY_CASE
    self.WORK_TIME=WORK_TIME
    self.SUBJECT=SUBJECT
    
    
    son1=int(input("Table Idsini kiriting. "))

    print("===========================================================")
    print("= 1.ID ==== 2.FNAME ==== 3.LNAME ==== 4.AGE ==== 5.BORN_Y =")
    print("===========================================================")

    print("===========================================================")
    print("= 6.EXPIENCE ==== 7.FAMCASE ==== 8.WORKTIME ==== 9.SUBJECT=")
    print("===========================================================")

    son=int(input("Iltimos, variantni tanlang. "))

       
    if son==1:
        dat=self.conn.execute(f"SELECT {ID}  FROM TEACHERS where ID={son1};")
        print(*dat)
    elif son==2:
      dat=self.conn.execute(f"SELECT {FNAME}  FROM TEACHERS where ID={son1};")
      print(*dat)
    elif son==3:
      dat=self.conn.execute(f"SELECT {LNAME}  FROM TEACHERS where ID={son1};")
      print(*dat)
    elif son==4:
      dat=self.conn.execute(f"SELECT {AGE}  FROM TEACHERS where ID={son1};")
      print(*dat) 
    elif son==5:
      dat=self.conn.execute(f"SELECT {BORN_YEAR}  FROM TEACHERS where ID={son1};")
      print(*dat)
    elif son==6:
      dat=self.conn.execute(f"SELECT {EXPERIENCE}  FROM TEACHERS where ID={son1};")
      print(*dat)   
    elif son==7:
      dat=self.conn.execute(f"SELECT {FAMILY_CASE}  FROM TEACHERS where ID={son1};")
      print(*dat)
    elif son==8:
      dat=self.conn.execute(f"SELECT {WORK_TIME}  FROM TEACHERS where ID={son1};")
      print(*dat)
    elif son==9:
      dat=self.conn.execute(f"SELECT {SUBJECT}  FROM TEACHERS where ID={son1};")
      print(*dat)
    else:
        print("Uzur, bunday variant topilmadi. ") 
  
  def update_data(self, ID,FNAME,LNAME,AGE,BORN_YEAR,EXPERIENCE,FAMILY_CASE,WORK_TIME,SUBJECT):

    self.ID=ID
    self.FNAME=FNAME
    self.LNAME=LNAME
    self.AGE=AGE
    self.BORN_YEAR=BORN_YEAR
    self.EXPERIENCE=EXPERIENCE
    self.FAMILY_CASE=FAMILY_CASE
    self.WORK_TIME=WORK_TIME
    self.SUBJECT=SUBJECT

    son1=int(input("Table Idsini kiriting. "))
        
    print("\t\t****************")
    print("\t\t**** ID _1. ****")
    print("\t\t****************")
    print("******************************************************")
    print("*  FNAME   ****  LNAME   ****   AGE    ****  BORN_Y  *")
    print("* click_2. **** click_3. **** click_4. **** click_5. *")
    print("******************************************************") 
    print("******************************************************")
    print("*  EXPER   **** FAMCASE  **** WORK_TI  **** SUBJECT  *")
    print("* click_6. **** click_7. **** click_8. **** click_9. *")
    print("******************************************************")
    
    num1=int(input("Variantdan birini tanlang... "))

    if num1==1: 
       id=int(input("Enter the Id of the teacher. "))
       self.conn.execute(f"UPDATE TEACHERS set ID='{id}' where ID='{son1}';")
    elif num1==2:   
       fname=input("Enter the Fname of the teacher. ")
       self.conn.execute(f"UPDATE TEACHERS set FNAME='{fname}' where ID='{son1}';")
    elif num1==3:
       lname=input("Enter the Lname of the teacher. ")
       self.conn.execute(f"UPDATE TEACHERS set LNAME='{lname}' where ID='{son1}';")
    elif num1==4:
       age=int(input("Enter the Age of the teacher. "))
       self.conn.execute(f"UPDATE TEACHERS set AGE='{age}' where ID='{son1}';")
    elif num1==5:
       born_year=int(input("Enter the Boran_year of the teacher. "))
       self.conn.execute(f"UPDATE TEACHERS set BORN_YEAR='{born_year}' where ID='{son1}';")
    elif num1==6:
       experience=input("Enter the Tajribasi of the teacher. ")
       self.conn.execute(f"UPDATE TEACHERS set EXPERIENCE='{experience}' where ID='{son1}';")
    elif num1==7:
       familiy_case=input("Enter the Oilaviy_holati of the teacher. ")
       self.conn.execute(f"UPDATE TEACHERS set FAMILY_CASE='{familiy_case}' where ID='{son1}';")
    elif num1==8:
       work_time=input("Enter the Work_time of the teacher. ")
       self.conn.execute(f"UPDATE TEACHERS set WORK_TIME='{work_time}' where ID='{son1}';")
    elif num1==9:
      subject=input("Enter the Subject of the teacher. ")
      self.conn.execute(f"UPDATE TEACHERS set SUBJECT='{subject}' where ID='{son1}';")
    else:
        print("Bunday option mavjud emas. ") 
    self.conn.commit()     
    print("It is done.") 

  
  def delete_one(self,  ID=None,FNAME=None,LNAME=None,AGE=None,BORN_YEAR=None,EXPERIENCE=None,FAMILY_CASE=None,WORK_TIME=None,SUBJECT=None):
        print("\t\t****************")
        print("\t\t**** ID _1. ****")
        print("\t\t****************")
        print("******************************************************")
        print("*  FNAME   ****  LNAME   ****   AGE    ****  BORN_Y  *")
        print("* click_2. **** click_3. **** click_4. **** click_5. *")
        print("******************************************************") 
        print("******************************************************")
        print("*  EXPER   **** FAMCASE  **** WORK_TI  **** SUBJECT  *")
        print("* click_6. **** click_7. **** click_8. **** click_9. *")
        print("******************************************************")

        num2=int(input("Qaysi option bo'yicha o'chirishni xoxlaysiz.  "))

        if num2==1:
            ID=int(input("Enter the id of teacher. "))
            self.conn.execute(f"delete from TEACHERS where ID='{ID}';")
        elif num2==2:
            FNAME=input("Enter the Fname of teacher. ")
            self.conn.execute(f"delete from TEACHERS where FNAME='{FNAME}';")
        elif num2==3:
            LNAME=input("Enter the Lname of teacher. ")
            self.conn.execute(f"delete from TEACHERS where LNAME='{LNAME}';")
        elif num2==4:
            AGE=int(input("Enter the Age of teacher. "))
            self.conn.execute(f"delete from TEACHERS where AGE='{AGE}';")
        elif num2==5:
            BORN_YEAR=input("Enter the Born_year of teacher. ")
            self.conn.execute(f"delete from TEACHERS where BORN_YEAR='{BORN_YEAR}';")
        elif num2==6:
            EXPERIENCE=input("Enter the Experience of teacher. ")
            self.conn.execute(f"delete from TEACHERS where EXPERIENCE='{EXPERIENCE}';")
        elif num2==7:
            FAMILY_CASE=input("Enter the Family_case of teacher. ")
            self.conn.execute(f"delete from TEACHERS where FAMILY_CASE='{FAMILY_CASE}';")  
        elif num2==8:
            WORK_TIME=input("Enter the Work_time of teacher. ")
            self.conn.execute(f"delete from TEACHERS where WORK_TIME='{WORK_TIME}';")
        elif num2==9:
            SUBJECT=input("Enter the Subject of teacher. ")
            self.conn.execute(f"delete from TEACHERS where SUBJECT='{SUBJECT}';")     

        self.conn.commit()    
        print("Muaffaqiyatli o'chirildi, berilgan ko'rsatma bo'yicha. ") 
  def allShow(self, ):
    dat=self.conn.execute("select * from TEACHERS")     
    for row in dat:
      print(*row)        
          
                                 
ustoz=Oqituvchi('pap1')
#ustoz.create_table()

print("********************************************************************")
print("* click_1. **** click_2. **** click_3. **** click_4. **** click_5. *")
print("* Add_per  **** Show_per **** Uppdate  ****  Delete  **** ShowALL  *")
print("********************************************************************")

num=int(input("Please, Select one. "))
if num==1: 
   ustoz=Oqituvchi('pap1') 
   while 1:
      id=int(input("Enter the Id of the teacher. "))
      fname=input("Enter the Fname of the teacher. ")
      lname=input("Enter the Lname of the teacher. ")
      age=int(input("Enter the Age of the teacher. "))
      born_year=int(input("Enter the Boran_year of the teacher. "))
      experience=input("Enter the Tajribasi of the teacher. ")
      familiy_case=input("Enter the Oilaviy_holati of the teacher. ")
      work_time=input("Enter the Work_time of the teacher. ")
      subject=input("Enter the Subject of the teacher. ")
   
      ustoz.add_person(id,fname,lname,age,born_year,experience,familiy_case,work_time,subject) 

elif num==2:

   ustoz.show_person('id','fname','lname','age','born_year','experience','familiy_case','work_time','subject')

elif num==3:   

   ustoz.update_data('id','fname','lname','age','born_year','experience','familiy_case','work_time','subject')

elif num==4:
  ustoz.delete_one('id','fname','lname','age','born_year','experience','familiy_case','work_time','subject')
elif num==5:
  ustoz.allShow()  










       
    




     

                            

    