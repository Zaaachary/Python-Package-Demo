# 交互式更新
import shelve
from person import Person

fieldnames = ('name', 'age', 'job', 'pay')
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key: break           # 键或者空行，空行退出
    if key in db:
        record = db[key]        # 更新存在的记录
    else:                       # 创建/保存新的记录
        record = Person(name='?', age='?')  
    for field in fieldnames:    # 依次对每个字段进行操作
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            setattr(record, field, eval(newtext))   # eval: 引号字符串
            # name  'zachary Lee'
    db[key] = record
db.close()