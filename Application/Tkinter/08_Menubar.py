import tkinter as tk



window = tk.Tk()
window.title('Menubar')
window.geometry('200x200')



lab = tk.Label(window,bg='yellow',width = 10,height= 3,text = 'empty')
lab.pack()
counter = 0
def do_job():
    global counter
    lab.config(text='do '+ str(counter))
    counter+=1

# 创建一个菜单栏（一个容器）
menubar = tk.Menu(window)
# 定义空菜单单元
filemenu = tk.Menu(menubar, tearoff=0)  # 不可拆分
# 在菜单单元里添加小菜单
filemenu.add_command(label = 'New', command = do_job)
filemenu.add_command(label = 'Open', command = do_job)
filemenu.add_command(label = 'Save', command = do_job)
filemenu.add_separator()        # 一条分割线
filemenu.add_command(label='Exit', command = window.quit)

# 将上面定义的空菜单命名为'File',放在菜单栏中
menubar.add_cascade(label = 'File', menu=filemenu)

# 和上面定义菜单一样，不过此处实在`File`上创建一个空的菜单
submenu = tk.Menu(filemenu)
# 给放入的菜单`submenu`命名为`Import`
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
# 这里和上面也一样，在`Import`中加入一个小菜单命令`Submenu1`
submenu.add_command(label="Submenu1", command=do_job)

window.config(menu=menubar)
window.mainloop()