from tkinter  import *
from tkinter import ttk
from PIL import Image, ImageTk
# image uchun pillow instal qilamiz

class Employee:

  def __init__(self,root) -> None:

    self.root=root
    self.root.geometry("1360x700+0+0")
    self.root.title('Data about Employees')

    #Variables
    self.var_dep=StringVar()
    self.var_name=StringVar()  
    self.var_designetion=StringVar()
    self.var_email=StringVar()
    self.var_address=StringVar()
    self.var_married=StringVar()
    self.var_dob=StringVar()
    self.var_doj=StringVar()
    self.var_gender=StringVar()
    self.var_country=StringVar()
    self.var_phone=StringVar()
    self.var_salary=StringVar()



    lbl_title=Label(self.root, text="Data about Employee",font=('times new room',30,'bold'),fg='darkblue',bg='white')
    lbl_title.place(x=0, y=0, width=1360, height=60)
    #img_logo
    img_logo=Image.open('images/emp.png')
    img_logo=img_logo.resize((50,50), Image.Resampling.LANCZOS)
    self.photo_logo=ImageTk.PhotoImage(img_logo)

    self.logo=Label(self.root,image=self.photo_logo)
    self.logo.place(x=380, y=0, width=50, height=50)

    #img_frame
    img_frame=Frame(self.root, bd=2, relief=RIDGE, bg='black')
    img_frame.place(x=5, y=55, width=1360, height=150)


    #img1
    img1=Image.open('images/emp2.jpg')
    img1=img1.resize((430,150), Image.Resampling.LANCZOS)
    self.photo1=ImageTk.PhotoImage(img1)

    self.img_1=Label(img_frame,image=self.photo1)
    self.img_1.place(x=0, y=0, width=430, height=150)

    #img2
    img2=Image.open('images/emp3.jpg')
    img2=img2.resize((430,150), Image.Resampling.LANCZOS)
    self.photo2=ImageTk.PhotoImage(img2)

    self.img_2=Label(img_frame,image=self.photo2)
    self.img_2.place(x=450, y=0, width=430, height=150)

    #img3
    img3=Image.open('images/emp4.jpg')
    img3=img3.resize((440,150), Image.Resampling.LANCZOS)
    self.photo3=ImageTk.PhotoImage(img3)

    self.img_3=Label(img_frame,image=self.photo3)
    self.img_3.place(x=900, y=0, width=445, height=150)

    #main_frame
    main_frame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
    main_frame.place(x=5, y=200, width=1360, height=540)

    #upper_frame
    upper_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text='Employee_information',font=('times new room',12,'bold'),fg='red',bg='white')
    upper_frame.place(x=5, y=5, width=1330, height=230)

    #lable and entry field
    lbl_dep=Label(upper_frame, text='Depertment:',font=('arial',11,'bold'),bg='#555')
    lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

    combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11,'bold'),width=17, state='readonly')
    combo_dep['value']=('Select Depertment', 'HR', 'Software_engineer', 'Manager')
    combo_dep.current(0)
    combo_dep.grid(row=0, column=1,sticky=W, padx=2, pady=10)

    #name
    lbl_name=Label(upper_frame, text='Name:',font=('arial',11,'bold'),bg='#555')
    lbl_name.grid(row=0, column=2, padx=2,pady=7, sticky=W)

    text_name=ttk.Entry(upper_frame,textvariable=self.var_name, width=22,font=('arial',11,'bold'))
    text_name.grid(row=0, column=3, padx=2, pady=7)

    #Desigination

    lbl_designetion= Label(upper_frame, text='Designetion:',font=('arial',11,'bold'),bg='#555')
    lbl_designetion.grid(row=1, column=0, sticky=W, padx=2,pady=7)

    text_designetion=ttk.Entry(upper_frame,textvariable=self.var_designetion,width=22,font=('arial',11,'bold'))
    text_designetion.grid(row=1, column=1, padx=2, pady=7)

    #Email

    lbl_email=Label(upper_frame, text='Email:',font=('arial',11,'bold'),bg='#555')
    lbl_email.grid(row=1, column=2, sticky=W, padx=2, pady=7)

    text_email=ttk.Entry(upper_frame,textvariable=self.var_email, width=22,font=('arial',11,'bold'))
    text_email.grid(row=1, column=3, padx=2, pady=7)

    #Address

    lbl_Address=Label(upper_frame, text='Address:',font=('arial',11,'bold'),bg='#555')
    lbl_Address.grid(row=2, column=0, sticky=W, padx=2, pady=7)

    text_Address=ttk.Entry(upper_frame,textvariable=self.var_address, width=22,font=('arial',11,'bold'))
    text_Address.grid(row=2, column=1, padx=2, pady=7)

    #Married
    lbl_marreid=Label(upper_frame, text='Married State:',font=('arial',11,'bold'),bg='#555')
    lbl_marreid.grid(row=2, column=2, padx=2, sticky=W)

    combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial',11,'bold'),width=17, state='readonly')
    combo_dep['value']=('Married', 'Unmarried')
    combo_dep.current(0)
    combo_dep.grid(row=2, column=3,sticky=W, padx=2, pady=7)
    
    #Dob
    lbl_dob=Label(upper_frame, text='DOB:',font=('arial',11,'bold'),bg='#555')
    lbl_dob.grid(row=3, column=0, sticky=W, padx=2, pady=7)

    text_dob=ttk.Entry(upper_frame,textvariable=self.var_dob, width=22,font=('arial',11,'bold'))
    text_dob.grid(row=3, column=1, padx=2, pady=7)

    #DOJ
    lbl_doj=Label(upper_frame, text='DOJ:',font=('arial',11,'bold'),bg='#555')
    lbl_doj.grid(row=3, column=2, sticky=W, padx=2, pady=7)

    text_doj=ttk.Entry(upper_frame, textvariable=self.var_doj,width=22,font=('arial',11,'bold'))
    text_doj.grid(row=3, column=3, padx=2, pady=7)

    #gender
    lbl_marreid=Label(upper_frame, text='Gender:',font=('arial',11,'bold'),bg='#555')
    lbl_marreid.grid(row=4, column=0, padx=2, sticky=W)

    combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',11,'bold'),width=17, state='readonly')
    combo_dep['value']=('Male', 'Female','Other')
    combo_dep.current(0)
    combo_dep.grid(row=4, column=1,sticky=W, padx=2, pady=7)

    #phone
    lbl_phone=Label(upper_frame, text='Phone:',font=('arial',11,'bold'),bg='#555')
    lbl_phone.grid(row=4, column=2, sticky=W, padx=2, pady=7)

    text_phone=ttk.Entry(upper_frame,textvariable=self.var_phone, width=22,font=('arial',11,'bold'))
    text_phone.grid(row=4, column=3, padx=2, pady=7)

    #country
    lbl_country=Label(upper_frame, text='Country:',font=('arial',11,'bold'),bg='#555')
    lbl_country.grid(row=0, column=4, sticky=W, padx=2, pady=7)

    text_country=ttk.Entry(upper_frame,textvariable=self.var_country, width=22,font=('arial',11,'bold'))
    text_country.grid(row=0, column=5, padx=2, pady=7)

    #ctc
    lbl_ctc=Label(upper_frame, text='Salery(CTC):',font=('arial',11,'bold'),bg='#555')
    lbl_ctc.grid(row=2, column=4, sticky=W, padx=2, pady=7)

    text_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary, width=22,font=('arial',11,'bold'))
    text_ctc.grid(row=2, column=5, padx=2, pady=7)


    #button_frame
    main_button=Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
    main_button.place(x=1100, y=2, width=180, height=190)

    btn_add=Button(main_button, text='Save',font=('arial',12,'bold'), width=15, bg='blue',fg='yellow')
    btn_add.grid(row=0, column=0, padx=1, pady=5)

    
    btn_update=Button(main_button, text='Update',font=('arial',12,'bold'), width=15, bg='blue',fg='yellow')
    btn_update.grid(row=1, column=0, padx=1, pady=5)

    
    btn_delete=Button(main_button, text='Delete',font=('arial',12,'bold'), width=15, bg='blue',fg='yellow')
    btn_delete.grid(row=2, column=0, padx=1, pady=5)

    
    btn_clear=Button(main_button, text='Clear',font=('arial',12,'bold'), width=15, bg='blue',fg='yellow')
    btn_clear.grid(row=3, column=0, padx=1, pady=5)


    #down_frame
    dwon_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text='Employee_information',font=('times new room',11,'bold'),fg='red',bg='white')
    dwon_frame.place(x=5, y=240, width=1330, height=230)

    #search_frame
    self.var_com_search=StringVar()
    search_frame=LabelFrame(dwon_frame, bd=2, relief=RIDGE, text=' Search Employee_information',font=('times new room',10,'bold'),fg='red',bg='white')
    search_frame.place(x=5, y=0, width=1310, height=60)

    search_by=Label(search_frame, text='Search By:',font=('arial',12,'bold'), width=15, bg='blue',fg='yellow')
    search_by.grid(row=0, column=0, padx=5, sticky=W)


    #search
    
    combo_txt_search=ttk.Combobox(search_frame,font=('arial',11,'bold'),width=17, state='readonly')
    
    combo_txt_search['value']=('Select_option', 'Name','Phone')
    combo_txt_search.current(0)
    combo_txt_search.grid(row=0, column=1,sticky=W, padx=5)

    txt_search=ttk.Entry(search_frame, width=22,font=('arial',11,'bold'))
    txt_search.grid(row=0, column=2, padx=5)

    btn_search=Button(search_frame, text='Search',font=('arial',11,'bold'), width=15, bg='blue',fg='yellow')
    btn_search.grid(row=0, column=3, padx=3)
 
    btn_ShowALL=Button(search_frame, text='ShoWAll',font=('times new roman',11,'bold'), width=15, bg='blue',fg='yellow')
    btn_ShowALL.grid(row=0, column=4, padx=3)

    stayhome=Label(search_frame, text='Doctor:',font=('arial',12,'bold'), width=15, bg='blue',fg='red')
    stayhome.place(x=1100, y=0, width=200, height=30)

    img_logo=Image.open(r"images/emp5.jpg")
    img_logo=img_logo.resize((50,30), Image.Resampling.LANCZOS)
    self.photoimg_logo=ImageTk.PhotoImage(img_logo)

    self.logo=Label(search_frame,image=self.photoimg_logo)
    self.logo.place(x=1040, y=0, width=50, height=30)

    #===========Employee table=========================

    #table_frame
    table_frame=Frame(dwon_frame , bd=2, relief=RIDGE)
    table_frame.place(x=5, y=60, width=1310, height=138)

    scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

    self.employee_table=ttk.Treeview(table_frame, columns=('dep','name','designetion','email','address','married','dob', 'doj', 'gender','country', 'phone','salary'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    scroll_x.config(command=self.employee_table.xview)
    scroll_y.config(command=self.employee_table.yview)

    self.employee_table.heading('dep', text='Department')
    self.employee_table.heading('name', text='Name')
    self.employee_table.heading('designetion',text='Designition')
    self.employee_table.heading('email', text='Email')
    self.employee_table.heading('address', text='Address')
    self.employee_table.heading('married', text='Married')
    self.employee_table.heading('dob', text='DOB')
    self.employee_table.heading('doj', text='DOJ')
    self.employee_table.heading('gender', text='Gender')
    self.employee_table.heading('country', text='Country')
    self.employee_table.heading('phone', text='Phone')
    self.employee_table.heading('salary', text='Salary')

    self.employee_table['show']='headings'

    self.employee_table.column("dep", width=100)
    self.employee_table.column("name", width=100)
    self.employee_table.column("designetion",width=100)
    self.employee_table.column("email", width=100)
    self.employee_table.column("address", width=100)
    self.employee_table.column("married", width=100)
    self.employee_table.column("dob", width=100)
    self.employee_table.column("doj", width=100)
    self.employee_table.column("gender", width=100)
    self.employee_table.column("country", width=100)
    self.employee_table.column("phone", width=100)
    self.employee_table.column("salary", width=100)


    self.employee_table.pack(fill=BOTH, expand=1)

    #============Function declaration==============



    



    









if  __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

    
