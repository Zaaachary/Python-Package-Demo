import tkinter as tk

# 创建主窗口
window = tk.Tk()
window.title('课程表')
window.geometry('300x300')

# 创建一个label用于显示
var1 = tk.StringVar()     # 创建变量
label1 = tk.Label(window,bg='yellow',width=15,textvariable=var1)
label1.pack()

# 创建一个方法用于按钮的点击事件
def print_selection():
    value = listb.get(listb.curselection())
    var1.set(value)

# 创建一个按钮
bt1 = tk.Button(
    window,
    text = "print selection",
    width = 15,height = 2,
    command = print_selection
)
bt1.pack()

# 创建一个ListBox
var2 = tk.StringVar()
var2.set(('数据结构','计算机组成原理','操作系统','计算机网络'))
listb = tk.Listbox(window, listvariable = var2)

# 创建一个list并将值循环添加到listbox里
list_item = {'图像工程概论','数字信号处理','Verilog硬件描述语言'}
for item in list_item:
    # for循环从最后位置插入item
    listb.insert('end',item)
listb.insert(1,'微机原理(0)')
listb.insert(2,'汇编语言')
# listb.delete(2)
listb.pack()

window.mainloop()