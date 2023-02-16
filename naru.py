from tkinter import *
from random import *

root = Tk()
root.title("Тестовое приложение")
root.geometry("1280x720")
root.resizable(width=False, height=False)
root["bg"] = "black"

def add():
    e.insert(END , "Hello")




e = Entry(root, show='*')
e.pack()

def dele():
    e.delete(0, END)

def get():
    label1['text'] = e.get()

btn2 = Button(root, font="Arial 15", text='insert', command=add)
btn2.pack()

btn3 = Button(root, font="Arial 15", text='delete', command=dele)
btn3.pack()

btn4 = Button(root, font="Arial 15", text='get', command=get)
btn4.pack()

label1 = Label(root, bg='black', fg='white')
label1.pack()






root.mainloop()