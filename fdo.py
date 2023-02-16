import tkinter as tk
from tkinter import messagebox
def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value)==1:
        value = value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif  '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)

def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value+value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание','Нужно вводить только цифры! Вы ввели другие символы.')
        calc.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!!!')
        calc.insert(0, 0)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0,0)




def make_digit_button(digit, color: str):
    return tk.Button(text=digit, bg=color, font=('Arial',10), command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation,font=('Arial',10), fg='blue', command=lambda: add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation,font=('Arial',10), fg='blue', command=calculate)

def make_clear_button(operation):
    return tk.Button(text=operation,font=('Arial',10), fg='blue', command=clear)



def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()

win = tk.Tk()
win.geometry(f"241x241+93+193")
win['bg'] = 'black'
win.title('Калькулятор')

win.bind('<Key>', press_key)






calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial',10), width=13)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we')







make_digit_button('1', '#87CEFA').grid( row=1, column=0,stick='wens',padx=4,pady=2)
make_digit_button('2','#6495ED').grid(row=1, column=1,stick='wens',padx=4,pady=2)
make_digit_button('3','#ADD8E6').grid(row=1, column=2,stick='wens',padx=4,pady=2)
make_digit_button('4','#6495ED').grid(row=2, column=0,stick='wens',padx=4,pady=2)
make_digit_button('5','#ADD8E6').grid(row=2, column=1,stick='wens',padx=4,pady=2)
make_digit_button('6','#87CEFA').grid(row=2, column=2,stick='wens',padx=4,pady=2)
make_digit_button('7','#ADD8E6').grid(row=3, column=0,stick='wens',padx=4,pady=2)
make_digit_button('8','#00BFFF').grid(row=3, column=1,stick='wens',padx=4,pady=2)
make_digit_button('9','#6495ED').grid(row=3, column=2,stick='wens',padx=4,pady=2)
make_digit_button('0','#87CEFA').grid(row=4, column=0,stick='wens',padx=4,pady=2)

make_operation_button('+').grid(row=1, column=3,stick='wens',padx=1,pady=2)
make_operation_button('-').grid(row=2, column=3,stick='wens',padx=1,pady=2)
make_operation_button('/').grid(row=3, column=3,stick='wens',padx=1,pady=2)
make_operation_button('*').grid(row=4, column=3,stick='wens',padx=1,pady=2)

make_calc_button('=').grid(row=4, column=2,stick='wens',padx=1,pady=2)
make_clear_button('C').grid(row=4, column=1,stick='wens',padx=1,pady=2)



win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)

win.grid_rowconfigure(1,minsize=40)
win.grid_rowconfigure(2,minsize=40)
win.grid_rowconfigure(3,minsize=40)
win.grid_rowconfigure(4,minsize=40)





















win.mainloop()





