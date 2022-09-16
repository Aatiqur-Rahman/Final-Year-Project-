from asyncio import windows_events
from tkinter import *
window=Tk()
# add widgets here

window.title('Hello Python')
window.geometry("300x200+10+20")

image_icon=PhotoImage(file="logo.jpg") 
window.iconphoto(False,image_icon)

logo=PhotoImage(file="logo.png") 
Label(window,image=logo, bg="#2f4155").place(x=10,y=0)

window.mainloop()