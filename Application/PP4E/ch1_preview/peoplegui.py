"""
图形界面，用于查看和更新村粗在shelve中的类实例
该shelve保存在脚本运行的机器上，可能是一个或多个本地文件
"""
from tkinter import *
from tkinter.messagebox import showerror, showinfo
import shelve

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')   # 字段

def makeWidgets():
    global entries          # 全局输入字段列表
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for(ix, label) in enumerate(('key',) + fieldnames):
        # 循环生成每个键的 标签和输入框
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent    # entries中每个label对应一个ent
    Button(window, text="Fetch", command=fetchRecord).pack(side=LEFT)
    Button(window, text="Update", command=updateRecord).pack(side=LEFT)
    Button(window, text="Quit", command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]        # 使用键获取数据，并在GUI中显示
    except:
        showerror(title='Error', message="No such Key!")
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))  # 显示从shelve中获得的字段值

def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]                        # 更新已有记录
    else:
        from person import Person               # 在该键值下生成/保存新记录
        record = Person(name='?', age='?')      # eval：字符串必须用引号引起来
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record
    showinfo(title='succeed', message='Record saved')


if __name__ == "__main__":
    global db
    db = shelve.open(shelvename)        # 作为全局变量打开
    window = makeWidgets()
    window.mainloop()
    db.close()