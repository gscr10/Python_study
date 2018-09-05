name1 = "小郭"
name2 = "小乔"


def love(a, b):   # 函数定义上方空2行
	"""说爱你"""    # 函数的说明文档

	print("%s love %s" % (a, b))
	return (a + b) 

love(name1,name2)
love_you = love(name2,name1)
print(love_you)

# 函数的嵌套调用


def test1():
	
	print("-" * 10)

def test2():
	
	print("*" * 10)
	test1()
	print("+" * 10)

test2()




# 打印分割线练习
def print_line(char,num):
	
	print(char * num)

print_line("-", 25)


def print_lines(char,num):
	"""打印多行分割线

	:param char:分隔线使用的字符
	:param num:分隔线重复的次数
	"""

	row = 0
	while row <= 5:
		print_line(char,num)
		row += 1

print_lines("love",25)


# 函数的返回值

# 利用元组返回多个值
def measure():
	"""测量温度湿度"""

	print("start...")
	temp = 39
	wetness = 50
	print("end...")

	# 如果返回的是元组，小括号可以省略
	# return (temp,wetness)
	return  temp,wetness

result = measure()
print("temp=%d  wetness=%d" % (result[0],result[1]))

# 可以使用多个变量一次接受函数的返回值
# 变量个数应该与元组中元素个数一致
g_temp, g_wetness = measure()
print("Temp=%d  Wetness=%d" % (g_temp,g_wetness))

# 交换两个变量的值
# python独有，利用元组
a = 1
b = 2
c = 3
print("a=%d  b=%d c=%d" % (a,b,c))
a, b, c = b, c, a
print("a=%d  b=%d c=%d" % (a,b,c))

# 函数内部通过赋值语句改变形参的值，不会影响实参的值，不论形参可变还是不可变
# 函数内部使用方法修改可变参数，会影响实参的值
def demo(list):
	list.append(11)
	return list
g_list = [4, 5, 6]
print(g_list)
demo(g_list)
print(g_list)

# +=
# 对于列表使用+=不会做相加再赋值的操作，而是调用extend()方法
def demo(num, num_list):
	num += num
	num_list += num_list
	num_list.extend(num_list)
	print(num)
	print(num_list)
g_num = 9
g_num_list = [1, 2, 3]
demo(g_num, g_num_list)
print(g_num)
print(g_num_list)


# 缺省参数
def sex(name, title="", gender=True):
	# 在定义是指定默认值即可
	# 需在定义参数的末尾
	# 调用带有多个缺省值的函数时要指定参数名
	gender_text = "男生"
	if not gender:
		gender_text = "女生"
	print("[%s]%s 是 %s" % (title, name, gender_text))
# 假设男生多
sex("小马")
sex("小美",gender=False)
