from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk


root = Tk()
root.title('White_Board')
root.geometry("1050x570+150+50")
root.configure(bg="#555555")
root.resizable(False,False)
  
current_x=0
current_y=0
color='black'

def locate_xy(work):
    global current_x, current_y

    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x, current_y

    canvas.create_line((current_x,current_y.x,work.y), width=2, fill=color)   
    current_x =  work.x
    current_y = work.y

def show_color(x):
    global color

    x=color

def new_canvans():

    canvas.delete('all')
    display_pro()         

#icon

image_icon=PhotoImage(file="pen.png")
root.iconphoto(False,image_icon)

color=Canvas(root, bg="#ffffff",width=40,height=400,bd=0)
color.place(x=30,y=50)



def display_pro():
  id = color.create_rectangle((10,10,30,30),fill='black')
  color.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

  id = color.create_rectangle((10,40,30,60),fill='yellow')
  color.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

  id = color.create_rectangle((10,70,30,90),fill='red')
  color.tag_bind(id, '<Button-1>',lambda x: show_color('red'))

  id = color.create_rectangle((10,110,30,130),fill='pink')
  color.tag_bind(id, '<Button-1>', lambda x: show_color('pink'))

  id = color.create_rectangle((10,140,30,160),fill='white')
  color.tag_bind(id, '<Button-1>', lambda x: show_color('white'))

  id = color.create_rectangle((10,170,30,190),fill='blue')
  color.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

  id = color.create_rectangle((10,200,30,220),fill='green')
  color.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

display_pro()  

eraser=PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="#f2f3f5",width=32,height=20).place(x=31,y=400)

canvas=Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)

root.mainloop()