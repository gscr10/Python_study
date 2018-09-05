# 方法重写
# 当父类中的方法不能满足子类的要求是需要重写

class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("飞起来")

    # 覆盖  在子类中定一个和父类中同名的方法
    def bark(self):
        print("叫起来和神一样")

        # 扩展
        # 1.针对子类中特有的需求，编写代码
        print("这是扩展后的叫声")

        # 2.使用super（），调用原父类中的方法
        super().bark()

        # 也可使用 父类.方法（self）调用父类方法
        # 不建议使用  若错写为子类名，会造成死循环
        Dog.bark(self)

        # 3.增加其他子类的代码
        print("增加的叫声")


xtq = XiaoTianQuan()

# 如果子类中重写了父类的方法，则调用时会调用重写
xtq.bark()
