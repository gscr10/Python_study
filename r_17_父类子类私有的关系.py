class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的公有方法")
        print("父类的私有属性%d" % self.__num2)
        self.__test()



class B(A):

    def demo(self):

        # 1.子类方法中不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)

        # 2.子类中不能调用父类的私有方法
        # self.__test()
        pass

        # 3.可以访问父类的公有属性
        print( "访问父类的公有属性 %d" % self.num1)

        # 4.可以访问父类的公有方法
        # 通过父类的公有方法间接访问父类的私有属性和私有方法
        self.test()
        




# 创建一个对象
b = B()
print(b)

print(b.num1)

# 在外界不允许访问对象的私有属性和方法
# print(b.__num2)
# b.__test()

b.demo()
