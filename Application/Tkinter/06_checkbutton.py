import tkinter as tk

window = tk.Tk()
window.title('checkbutton')
window.geometry('200x300')


l = tk.Label(window, text='empty',width=20,height=3)
l.pack()

def print_selection():
    # varx.get()获取varx获得的变量值
    if (var1.get() == 1) & (var2.get() == 0):   #如果选中第一个选项，未选中第二个选项
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1): #如果选中第二个选项，未选中第一个选项
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):  #如果两个选项都未选中
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')             #如果两个选项都选中

var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(
    window, text = 'Python',
    variable = var1,
    # 选中后 onvalue放入var1
    onvalue = 1,
    offvalue = 0,
    command = print_selection
)
c2 = tk.Checkbutton(
    window, text = 'C++',
    variable = var2,
    onvalue = 1,
    offvalue = 0,
    command = print_selection
)

c1.pack()
c2.pack()


window.mainloop()