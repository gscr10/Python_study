# 异常

# 捕获异常
# 对某些代码执行不能确定是否正确
try:
    # 不能确定正确执行的代码
    num = int(input("请输入一个整数："))
except:
    # 如果错误，将执行下面代码，程序不会停
    print("请输入正确的整数")

print("-" * 20)


# 针对错误类型捕获异常
# 1.提示用户输入一个整数
# 2.使用数字8 除以用户输入的整数并输出

try:
    num1 = int(input("输入一个整数："))
    result = 8 / num1
    print(result)

except ValueError:
    print("请输入正确的整数")

# except ZeroDivisionError:
#     print("除0错误")

# 捕获位置错误
except Exception as result:
    print("未知错误 %s" % result)

# 异常捕获的完整代码
else:
    # 没有异常才会执行的代码
    print("尝试成功")

finally:
    # 无论是否有异常，都会执行的代码
    print("无论是否有异常，都会执行")

print("-" * 20)



# 异常的传递
# 当函数/方法 执行出现异常，会将异常传递给函数/方法 的调用一方
# 如果传递到主程序，仍没有处理异常，程序才会被终止

def demo1():
    return int(input("输入整数："))

def demo2():
    return demo1()

# 利用异常的传递性，在主程序中捕获异常
try:
    print(demo2())
except Exception as result:
    print("未知错误 %s" % result)



# 抛出异常
# 1.创建一个Exception 的对象
# 2.使用raise 关键字抛出异常对象

# 提示用户输入密码，长度小于8，抛出异常
def input_password():

    # 1.提示用户输入密码
    password = str(input("请输入密码【不少于8位】："))

    # 2.判断密码长度 >=8 返回用户输入的密码
    if len(password) >= 8:
        return password
    # 3.如果 <8 主动抛出异常
    else:
        print("主动抛出异常")
        # 1)创建异常对象 - 可以使用错误信息字符串作为参数
        ex = Exception("密码长度不够")
        # 2）主动抛出异常
        raise ex

# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)
    

