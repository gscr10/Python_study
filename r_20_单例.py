# 单例的设计模式
# 让类创建的对象在体统中只有一个唯一的实例
# 每次执行 类名（） 返回对象时，内存地址是相同的

# __new__  是object基类的内置今天方法
# 1.在内存中分配空间
# 2.返回对象的引用

class MusicPlayer(object):


    # 定义类属性，记录第一个创建对象的引用
    instance = None

    # 定义类属性，记录是否执行初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1.判断类属性是否为空对象
        if cls.instance is None:

            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance


        # # 1.创建对象时，new方法会被自动调用
        # print("创建对象，分配空间")
        #
        # # 2.为对象分配空间
        # instance = super().__new__(cls)
        #
        # 3.返回对象的引用, 若不返回，初始化不能调用
        # return instance

    # 让初始化动作只执行1次
    def __init__(self):

        # 1.判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return

        # 2.若没有执行，执行动作
        print("播放器初始化")

        # 3.修改类属性的标记
        MusicPlayer.init_flag = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)


