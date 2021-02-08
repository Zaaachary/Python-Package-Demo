"""
peoplegui 的升级版本  db, entries 全卷变量->参数传递
"""
from tkinter import *
from tkinter.messagebox import showerror, showinfo
import shelve

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')   # 字段

def makeWidgets(db):
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}      # 输入字段列表
    for(ix, label) in enumerate(('key',) + fieldnames):
        # 循环生成每个键的 标签和输入框
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent    # entries中每个label对应一个ent
    Button(window, text="Fetch", command=(lambda: fetchRecord(db, entries))).pack(side=LEFT)
    Button(window, text="Update", command=(lambda: updateRecord(db, entries))).pack(side=LEFT)
    Button(window, text="Quit", command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord(db, entries):
    key = entries['key'].get()
    try:
        record = db[key]        # 使用键获取数据，并在GUI中显示
    except:
        showerror(title='Error', message="No such Key!")
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))  # 显示从shelve中获得的字段值

def updateRecord(db, entries):
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
    db = shelve.open(shelvename)
    window = makeWidgets(db)
    window.mainloop()
    db.close()