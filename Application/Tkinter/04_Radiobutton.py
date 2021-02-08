import tkinter as tk

window = tk.Tk()
window.title("RadioButton")
window.geometry('250x300')

# 定义var
var = tk.StringVar()
Lab = tk.Label(window, bg='green',width=20,text='empty')
Lab.pack()

def print_selection():
    Lab.config(text='you have selected ' + var.get())# var获取选中

r1 = tk.Radiobutton(
    window, 
    text='Option A',
    variable=var, value='A',    # 选中时，A 放入var中
    command = print_selection
    )
r1.pack()
r2 = tk.Radiobutton(
    window, text='Option B',
    variable=var, value='B',
    command=print_selection
    )
r2.pack()
r3 = tk.Radiobutton(
    window, text='Option C',
    variable=var, value='C',
    command=print_selection
    )
r3.pack()

window.mainloop()