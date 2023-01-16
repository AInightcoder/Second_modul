import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=100, height=60, image="buttons_PNG183.png", command=r.destroy)
button.pack()
r.mainloop()
