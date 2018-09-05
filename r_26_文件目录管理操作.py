# 文件目录操作
# 导入 os模块

import os

# 文件操作
os.rename("test.txt", "Test.txt")
# os.remove()

# 目录操作
print(os.listdir("."))



# eval函数
# 将字符串当成有效的表达式，并返回计算结果
# 不要使用eval函数直接转换 input 的结果


# 案例：计算器
input_str = input("请输入算术题：")
print(eval(input_str))