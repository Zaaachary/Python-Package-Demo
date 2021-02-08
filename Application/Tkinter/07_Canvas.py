import tkinter as tk

window = tk.Tk()
window.title('Canvas')
window.geometry('400x400')


# 创建画布
canvas = tk.Canvas(window,bg='blue',height=200,width=400)
# 创造变量存放ins.gif图片
image_file = tk.PhotoImage(file='image/ins.gif')
image = canvas.create_image(10,10,anchor='nw',image = image_file)   # n,ne,se,s,sw,w,nw,center
x0, y0, x1, y1= 50, 50, 80, 80

line = canvas.create_line(x0, y0, x1, y1)   # 绘制直线
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  #创建一个圆，填充色为`red`红色
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)  #创建一个扇形
rect = canvas.create_rectangle(100,100,150,150)   #创建一个矩形(x1,y1,x2,y2)

canvas.pack()

def movebutton():
    canvas.move(rect,0,4)

def movetop():
    canvas.move(rect,0,-4)


bt1 = tk.Button(window,text='↑',width=5,height=2,command=movetop)
bt2 = tk.Button(window,text='↓',width=5,height=2,command=movebutton)

bt1.pack()
bt2.pack()


window.mainloop()