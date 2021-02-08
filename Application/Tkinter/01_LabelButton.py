import tkinter as tk

window = tk.Tk()
window.title('tkinter window')
window.geometry('200x100')

var = tk.StringVar()    # 文字变量储存器
var.set("Tk is so cool!")
hide = False    # 默认初始不为隐藏

def hide_text():
    global hide
    if hide == False:
        hide = True
        var.set('')
    else:
        hide = False
        var.set("TK is so cool!")




# 窗口内容
l = tk.Label(
    window,
    textvariable=var,
    bg='green',
    font=('Arial',12),
    width=15,height=2
    )

b = tk.Button(
    window,
    text = 'hide or show',
    width = 15, height = 2,
    command = hide_text
)

# 固定窗口位置
l.pack()
b.pack()




window.mainloop()
