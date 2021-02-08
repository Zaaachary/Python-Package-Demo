import tkinter as tk

window = tk.Tk()
window.title('scale')
window.geometry('300x250')

def print_selection(v):
    l.config(text='you have selected '+ v)


l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


scal = tk.Scale(
    window, label='try it',
    from_ = 5, to=11,
    orient = tk.HORIZONTAL,
    length = 200,           # width 以字符为单位， length以像素为单位
    showvalue = 1,          # 滚动条上方显示数据 0不显示
    tickinterval = 2,       # 坐标间隔
    resolution = 0.01,      # 精确度
    command = print_selection
)
scal.pack()

window.mainloop()