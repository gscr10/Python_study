# 面向对象三个属性：封装、继承、多态
# 封装 将属性和方法封装到一个类中
# 继承 实现代码重用
# 多态 不同的对象调用相同的代码，产生不同的执行结果，增加代码的灵活度

# 单继承

class Animal():
	"""docstring for Animal"""
	def eat(self):
		print("吃")

	def drink(self):
		print("喝")

	def run(self):
		print("跑")

	def sleep(self):
		print("睡")


# 继承 class 类名（父类）
# 子类享受父类中已经封装的属性和方法
class Dog(Animal):

	# def eat(self):
	# 	print("吃")

	# def drink(self):
	# 	print("喝")

	# def run(self):
	# 	print("跑")

	# def sleep(self):
	# 	print("睡")

	def bark(self):
		print("汪汪叫")


# 继承的传递性
class XiaoTianQuan(Dog):

	def fly(self):
		print("飞起来")


class Cat(Animal):

	def catch(self):
		print("抓老鼠")


# 创建一个对象  狗对象
wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()

# 创建一个对象  哮天犬
xtq = XiaoTianQuan()
xtq.fly()
xtq.bark()
xtq.eat()

# 没有继承关系不能调用方法
# xtq.catch()



# 多继承
# 让子类共同具有多个父类的属性和方法
# 如果父类之间有同名的属性和方法，尽量避免使用多继承
#   

class A:
	
	def test(self):
		print("A---test 方法")
	
	def demo(self):
		print("A---demo 方法")


class B:
	
	def test(self):
		print("B---test 方法")
	
	def demo(self):
		print("B---demo 方法")


class C(B, A):

	pass

# 创建子类对象
c = C()
c.test()
c.demo()

# 方法搜索顺序 MRO
print(C.__mro__)

