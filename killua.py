from tkinter import *
from random import *



root = Tk()
root.title("Тестовое приложение")
root.geometry("500x500")
root.resizable(width=False, height=False)
root["bg"] = "black"

label1 = Label(root, text='Привет', fg='white', bg='brown', padx=20, pady=20)
label1.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5, relheight=0.5)







root.mainloop()