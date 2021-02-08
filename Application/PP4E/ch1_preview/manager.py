from person import Person

class Manager(Person):

    # 自定义构造函数
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)
        # Person.giveRaise(self, percent + bonus)


if __name__ == "__main__":
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName)
    tom.giveRaise(.20)
    print(tom.pay)


'''
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30000)
sue = Person('Sue Jones', 45, 40000)
tom = Manager('Tom Doe', 50, 50000)
db = [bob, sue, tom]
for obj in db:
    obj.giveRaise(.10)

for obj in db:
    print(obj.lastName(), '=>', obj.pay)

'''


'''
# person 添加 str方法后
tom = Manager('Tom Jones', 50)
print(tom)
# > <Manager => Tom Jones: None, 0>
'''