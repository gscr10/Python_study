# 多态  增加代码的灵活度
# 对不同的子类对象调用相同的父类方法，产生不同的结果
# 以继承和重写父类方法为前提
# 是调用的方法技巧，不会影响类的内部设计

class Dog(object):
	
	def __init__(self, name):
		self.name = name

	def game(self):
		print("[%s]普通狗玩耍" % self.name )

class XiaoTianQuan(Dog):

	def __init__(self, name):
		self.name = name

	def game(self):
		print("[%s]神犬天上飞" % self.name)

class Person(object):

	def __init__(self, name):
		self.name = name

	def game_with_dog(self, dog):
		print("%s正在和%s玩耍" % (self.name, dog.name))
		dog.game()


# 创建一个普通狗
wangcai = Dog("旺财")

# 创建一个哮天犬
xtq = XiaoTianQuan("哮天犬")

# 创建一个人
zhangsan = Person("张三")

zhangsan.game_with_dog(wangcai)
zhangsan.game_with_dog(xtq)


