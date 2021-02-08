from tkinter import *
from tkinter102OOP import MyGui

# 应用主窗口
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# 弹出窗口
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)               # 附加 myframe
mainwin.mainloop()