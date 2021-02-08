import tkinter as tk



# 从光标插入
def insert_point():
    var = ent.get()
    t.insert('insert',var)

# 从尾部插入
def insert_end():
    var = ent.get()
    t.insert('end', var)

# 窗口基本参数
window = tk.Tk()
window.title('Mr_StrawberrY')
window.geometry('200x200')

# 窗口内容
bt1 = tk.Button(
    window,text='insert point',
    width = 15,height = 2,
    command = insert_point
)
bt1.pack()

bt2 = tk.Button(
    window,
    text = "insert end",
    command = insert_end
)
bt2.pack()

ent = tk.Entry(window, show = '*')
ent.pack()

t = tk.Text(window, height = 2)
t.pack()

# 窗口循环
window.mainloop()