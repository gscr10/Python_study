class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s我的年龄是%d" % (self.name, self.__age))



xiaofang = Women("小芳")

# 私有属性在外界不能被直接访问
# print(xiaofang.__age)

# 私有方法不能在对象外界被访问
# xiaofang.__secret()

# python中只有伪私有，_类名__私有，不建议使用
xiaofang._Women__secret()
