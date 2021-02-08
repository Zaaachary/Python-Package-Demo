from PIL import Image,ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfilename

def choosepic():
    path_ = askopenfilename()
    im = Image.open(path_)
    img = ImageTk.PhotoImage(im)
    imLabel.config(image = img)
    imLabel.image=img
    


root = tk.Tk()
root.title('简单的图像处理')
root.geometry('1152x768')

imLabel=tk.Label(root)
imLabel.pack()
btn = tk.Button(root,text="显示图片",command=choosepic)
btn.pack()

root.mainloop()