from tkinter import *
root = Tk()
root.title("Паравозик")
root.geometry("1280x728")
root.resizable(width = False, height = False)
root.iconbitmap("icon.hello.ico")

def click():
    print("Привет")

label = Label(root,
             text = "Текст",
             font = ("Comic Sans MS", 20, "italic"),
             bg = "yellow",
             fg = "orange"

             )

label.pack()
img = PhotoImage(file="tutu.png")
l_logo = Label(root, image=img)
l_logo.pack()







root.mainloop()
