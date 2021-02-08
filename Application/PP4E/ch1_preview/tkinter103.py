from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s' % name)

# 设置图标和标题
top = Tk()
top.title('Echo')
top.iconbitmap('favicon.ico')

Label(top, text="Enter your name:").pack(side=TOP)
ent = Entry(top)    # 输入控件
ent.pack(side=TOP)
btn = Button(top, text="Submit", command=(lambda: reply(ent.get())))
# ↓reply会在按钮创建时候被调用 ↑使用lambda延迟对reply的调用
# btn = Button(top, text="Submit", command=reply(ent.get()))    
btn.pack(side=LEFT)
top.mainloop()