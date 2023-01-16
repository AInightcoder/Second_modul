import sqlite3

class University:

  def __init__(self, ) -> None:
    self.conn=sqlite3.connect('unidata.db')

  def createtable(self, ):

    self.conn.execute("""create table University(id   int,
    name              str,
    year              int,
    location          str,
    rate              int,
    opportunity       text,
    requirements      text); """)

    print('it is done')  

  def adduniversity(self,id: int,name: str,year: int,location: str,rate: int,opportunity: str,requirements: str):
    
    fsm = "insert into University(id,name,year,location,rate,opportunity,requirements) values"
    ssm = f"({id},'{name}',{year},'{location}',{rate},'{opportunity}','{requirements}');"
    allp=fsm+ssm
    self.conn.execute(allp)
    self.conn.commit()
    print("it is nice")

  def show_one(self,):

       det = self.conn.execute("select * from University ")
       print(*det)

  def delete_one(self, id):
      self.conn.execute(f"delete from University where id='{id}'")     
  
  def update_item(self, item_name,item, id):
    self.conn.execute(f"update University set '{item_name}' ='{item}' where id = '{id}' ")


