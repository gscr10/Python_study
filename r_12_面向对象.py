# 面向对象是一个更大的封装，根据职责在一个对象中封装对个方法
# 类  相当于一个模板，负责创建对象，具有属性、方法
# 对象  由类创造出来的一个具体存在
# 先有类，再有对对象。类只有一个，对象可以有多个

# 类的设计
# 1.类名 使用大驼峰命名法(每个单词首字母大写，之间没有下划线)
# 2.属性 有什么特征
# 3.方法 有什么样的行为

# 定义简单的类
class Cat:

    def eat(self):
        # 哪一个对象调用方法，self就是哪一个对象的引用
        print("%s  吃鱼" % self.name)

    def drink(self):
        print("%s  喝水" % self.name)


# 创建对象
tom = Cat()

tom.name = "Tom"  # 不推荐在类的外部给对象增加属性
tom.eat()
tom.drink()

print(tom)
addr = id(tom)
print("%x" % addr)

# 在创建对象
lazy_cat = Cat()

lazy_cat.name = "Lazy"
lazy_cat.drink()
lazy_cat.eat()
print(lazy_cat)

lazy_cat2 =lazy_cat
print(lazy_cat2)


# 初始化的方法，__init__ 定义类有哪些属性
class Dog:
    """这是一个类"""

    def __init__(self, new_name):

        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = new_name

    def eat(self):
        print("%s 爱吃肉" % self.name)

# 使用类名（）创建对象的时候，会自动调用初始化方法__init__
hot = Dog("Hot")
print(hot.name)

cool = Dog("Cool")
cool.eat()


# 内置方法和属性
# __del__ 方法  如果希望在对象被销毁前再做一些事，可以考虑__del__
# __str__方法
class R:
    def __init__(self, new_name):
        self.name = new_name
        print("%s is coming" % self.name)

    def __del__(self):
        print("%s going" % self.name)

    def __str__(self):

        # 必须返回一个字符串
        return "__str__方法[%s]" % self.name

# tom 是一个全局变量
tom = R("Tom")
print(tom.name)

# del 可以删除一个变量
# del tom
print("-" * 20)  # 在没有上句del时，在执行完这一句后tom变量回收

print(tom)


