import tkinter as tk

window = tk.Tk()
window.title('frame')
window.geometry('200x200')

tk.Label(window, text='on the window').pack()

# 在window上创建一个frame
frm = tk.Frame(window)
frm.pack()
# 在创建好的frame上创建两个frame 即frm下有两个frame
frm_left = tk.Frame(frm)
frm_right = tk.Frame(frm)
# 控制两个小的frm在大的相对位置
frm_left.pack(side='left')
frm_right.pack(side='right')

# 三个label定义在相应的frame上
tk.Label(frm_left, text='on the frm_left1').pack()
tk.Label(frm_left, text='on the frm_left2').pack()
tk.Label(frm_right, text='on the frm_right1').pack()
window.mainloop()
