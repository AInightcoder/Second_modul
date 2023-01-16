from university import University

go = University()
#go.createtable()

# go.adduniversity(1, 'MIT',1872, 'Cambridge', 1, 'Professional worker', 'SAT 1500+')
# go.adduniversity(2, 'Western University',1902, 'Washington', 8, 'beautiful ', 'IELTS 6+')
#go.show_one() 
go.delete_one(1)
go.show_one()
go.update_item('rate',10, 2)
go.show_one()

 