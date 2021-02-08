# 交互式查询
import shelve
fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)  # 查找字段中名称最长的
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key: break           # 键或者空行，空行退出
    try:
        record = db[key]        # 依据键获取记录
    except:
        print('No such key "%s"!' % key)
    else:
        for field in fieldnames:# 展示记录中各个字段
            # ljust(maxfield) 使输出的字符串左对齐
            # getattr 获取对象的属性
            print(field.ljust(maxfield), '=>', getattr(record, field))