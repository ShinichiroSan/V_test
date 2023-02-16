from tkinter import *
from random import *
hjjjjj

root = Tk()
root.title("Тестовое приложение")
root.geometry("1280x720")
root.resizable(width=False, height=False)
root["bg"] = "black"

l1 = Label(root, text='1', font='15', fg='white', bg='pink', width=8, height=4).pack(expand=1, anchor=W)


root.mainloop()