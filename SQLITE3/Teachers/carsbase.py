import sqlite3

class Cars:
    
    def __init__(self,pap) -> None:
        self.conn=sqlite3.connect('pap.db')

    def create_table(self):
       
          print ("Opened database successfully;")

          self.conn.execute('''CREATE TABLE Mashina
                  (id INT PRIMARY KEY     NOT NULL,
                  name            str     NOT NULL,
                  brand           str     NOT NULL,
                  year            int);''')
          print ("Table created successfully;")

    def add_moshina(self, id: int, name: str, brand: str, year: int) -> None:
        
        command_part1 = "insert into Mashina (id, name, brand, year)  values"
        command_part2 = f"({id}, '{name}', '{brand}',{year} );"
        command = command_part1+command_part2

        self.conn.execute(command)
        self.conn.commit()
        print ("Records created successfully;")

    def show_person(self, id, name, brand, year):
      dat=self.conn.execute("select * from Mashina where id =2")
      print(*dat)

    def uppdate_person(self, id, name, brand, year):
      fname=input('Enter the new_name: ')
      self.conn.execute(f"update Mashina set name='{fname}' where id =2 ") 
      self.conn.commit() 



letgo=Cars('pap')          
#letgo.create_table()
#letgo.add_moshina(2,'Jip','Chevrolet',2001)
letgo.show_person('id','name','brand','year')

#letgo.uppdate_person('id','name','brand','year')



                

        
