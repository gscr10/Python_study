# python的每个变量必须赋值才能正常使用
qq = 12345
print (qq)

"""
·变量类型

姓名：小乔
年龄：24
性别：是女生
身高：1.66m
体重：48kg

# 定义变量时不需要指定变量类型
"""
name = "乔宝宝"   # str
age = 24   # int
gender = True   # bool
height = 1.66   # float
weight = 48   #int

"""
变量类型
	·数字型:int  float  bool(非0既真)  complex(复数型)
	·非数字型：str  列表  元组  字典
"""
# type函数查看变量类型
type (gender)
print (type(gender))
print (type(2 ** 64))  # python3 中没有long型  Python2中有long型

# 变量的计算
# int之间可以直接计算
i = 100
f = 10.5
b = True
print (i + f)
print (f + b)
print (f * b)
print (i * b)
print (i + b)

# str之间可以拼接字符串
fist_name = "张"
last_name = "hah   "
print ((fist_name + last_name)*5+str(f)+"111111")
# 两个字符串不能做*法
a = "1.05"
b = "5.55"
a = float(a)
b = float(b)
print (a * b)

# 变量输入 input函数 ，均当做str
# password = input("请输入：")
# print ("密码是：" + password)
# print (type(password))

"""
变量的格式化输出
	%s 字符串
	%d 有符号的十进制整数，%06d表示整数显示位数，不足用0不全,%6d不足占位符不全
	%f 浮点数，%.02f表示小数点后显示2位
	%% 输出%
"""
print ("她的名字叫 %s,美美哒" % name)
print ("她的年龄叫 %010d,美美哒" % age)
print ("她的身高叫 %.10f,美美哒" % height)
print ("她在我心中占了 %.2f %%" % i)


# 变量的命名
	# 标识符：字母、下划线、数字，开头不能是数字 ，不能与关键字重名
	# 区分大小写
	# = 两侧都空格
	# 每个单词都使用小写字母，用下划线连接

# 关键字
import keyword   # import 可以导入一个“工具包”
# 输出关键字列表，进行查看
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 
'except', 'finally', 'for', 'from', 'global', 'if', 'import',
'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
"""
print (keyword.kwlist)  


# 局部变量和全局变量
# 函数不能直接修改全局变量的值
# 如果函数内部使用赋值语句，则是在函数内部定义一个局部变量
# 若在函数内部对全局变量进行修改，用global
# 全局变量应定义在所有函数上方
# 全局变量可以加上g_  gl_

g_num =10


def demo1():
    global g_num
    g_num = 99
    print("demo1  %d" % g_num)
    print("demo1  %d" % gl_num2)


def demo2():
    print("demo2  %d" % g_num)

gl_num2 = 100

demo1()
demo2()


