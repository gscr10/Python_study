# 封装  把属性和方法封装到一个抽象的类中
# 外界使用类创建对象，然后让对象调用方法
# 对象方法的细节都被封装在类的内部

# 小明爱跑步
# 1.小明体重75.0公斤
# 2.每次跑步减肥0.5公斤
# 3.吃东西增加1公斤


class Person:

    def __init__(self, name, weight):

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字是%s 体重是%.2f公斤" % (self.name, self.weight)

    def run(self, n):
        print("%s爱跑步，跑了%d次" % (self.name, n))

        while n > 0:
            self.weight -= 0.5
            n -= 1

    def eat(self, n):
        print("%s是吃货，吃了%d顿" % (self.name, n))

        while n > 0:
            self.weight += 1
            n -= 1


xiaoming = Person("小明", 100.0)
xiaoming.run(1)
xiaoming.eat(1)
print(xiaoming)

xiaomei = Person("小美", 50.0)
xiaomei.run(2)
xiaomei.eat(2)
print(xiaomei)
print(xiaoming)  # 属性互补不干扰


# 摆放家具
# 1.房子有户型、总面积、家具名称列表，新房子没有任何家具
# 2.家具有名字、占地面积，其中：床4 柜子2 餐桌1.5
# 3.将三种家具添加到房子中
# 4.打印房子时，输出户型、总面积、剩余面积、家具列表

class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]的占地面积为%.2f平米" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具列表
        self.item_list = []

    def __str__(self):

        # python 能将一对（）内的代码连接在一起
        return ("户型是:%s\n总面积:%.2f平米[剩余面积:%.2f平米]\n家具列表：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加%s" % item)
        # 如果超过房子面积提示不能添加家具
        if item.area > self.free_area:
            print("当前剩余%.2f平米，%s面积[%.2f平米]太大，无法添加"
                  % (self.free_area, item.name, item.area))
            return

        # 计算剩余面积
        self.free_area -= item.area

        # 家具添加到列表
        self.item_list.append(item.name)
        print("添加%s成功！" % item.name)


# 1.创建家具对象
bed = HouseItem("床", 4)
chest = HouseItem("柜子", 2.5)
table = HouseItem("桌子", 80)
print(bed)
print(chest)
print(table)

# 2.创建房子对象
my_home = House("两室一厅", 80)

# 3.添加家具
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)


# 一个对象的属性可以是另一个类创建的对象

# 案例：士兵突击
# 1.士兵许三多有一把M4
# 2.士兵可以开火
# 3.枪能够发射子弹
# 4.枪能够装填子弹--增加子数

class Gun:

    def __init__(self, modle):

        # 1.枪的型号
        self.modle = modle

        # 2.子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):

        # 1.判断子弹数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了..." % self.modle)

            return

        # 2.发射子弹 -1
        self.bullet_count -= 1

        # 3.提示发射信息
        print("[%s]突突突...[%d]" % (self.modle, self.bullet_count))


class Soldier:

    def __init__(self, name):
        self.name = name

        # 不知道设置初始值使用None关键字
        self.gun = None

    def fire(self):

        # 1.判断是否有枪
        # is和is not判断两个变量引用的对象是否为同一个
        # ==判断两个变量的值是否相等
        if self.gun is None:
            print("可怜的士兵%s还没有枪" % self.name)

            return

        # 2.高喊口号
        print("冲啊...[%s]" % self.name)

        # 3.装填子弹
        self.gun.add_bullet(50)

        # 4.发射子弹
        self.gun.shoot()


# 1.创建枪
m4 = Gun("M4")

# 2.创建许三多
xusanduo = Soldier("许三多")

xusanduo.gun = m4
xusanduo.fire()
