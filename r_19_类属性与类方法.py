# 类是一个特殊的属性

# 类属性 给类对象中定义的属性
# 通常记录 与这个类相关的特征
# 不用于记录具体对象的特征

class  Tool(object):

	# 使用赋值语句定义类属性
	count = 0

	def __init__(self, name):
		self.name = name

		# 让类属性的值 +1
		Tool.count += 1

# 创建工具对象
tool1 = Tool("1")
tool2 = Tool("2")
tool3 = Tool("3")

# 输出工具总数  类.类属性
print("类属性 工具总数%d" % Tool.count)

# 也可用 对象名.类属性  不推荐使用
print(tool1.count)

# 对象.类属性 若赋值会在对象内部添加一个实例属性
tool3.count = 99
print(tool3.count)
print(Tool.count)


# 类方法
class Bar(object):

	count = 0

	@classmethod
	def show_bar_count(cls):
		print("bar方法的数量是%d" % cls.count)

	def __init__(self, name):
		self.name = name

		Bar.count += 1


bar1 = Bar("1")
bar2 = Bar("2")
bar3 = Bar("3")

Bar.show_bar_count()



# 静态方法
class Dog(object):


	# 不需要访问类属性、实例属性时定义为静态方法
	@staticmethod
	def run():
		print("run ...")

# 通过 类名. 调用静态方法，不需要创建对象
Dog.run()



# 方法综合案例
"""
1.设计一个Game类
2.属性
	·定义一个类属性top_score记录游戏的历史最高分
	·定义一个实例属性play_name记录当前玩家的姓名
3.方法
	·静态方法show_help显示游戏帮助信息
	·类方法show_top_score显示历史最高分
	·实例方法start_game开始当前玩家游戏
4.主程序
	1）查看帮助信息
	2）产看历史最高分数
	3）创建游戏对象，开始游戏
"""

class Game(object):

	# 定义类属性
	top_score = 89

	def __init__(self,play_name):
		self.play_name = play_name

	@staticmethod
	def show_help():
		print("游戏帮助...")

	@classmethod
	def show_top_score(cls):
		print("当前最高分是%d" % cls.top_score)

	def start_game(self):
		print("玩家%s开始游戏" % self.play_name)

# 主程序
Game.show_help()
Game.show_top_score()

game = Game("张三")
game.start_game()

# 若既要访问实例属性，又要访问类属性，定义为实例方法
# 在实例方法中用 类名. 访问类属性


