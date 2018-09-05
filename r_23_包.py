# coding=utf-8
# 包  包含多个模块的特殊目录
# 目录下有一个特殊文件 __init__
# 命名方式和变量名一致，小写字母_
# 使用 import 可以导入包中所有模块


# 导入包
import r_23_package

r_23_package.send_message.send("hello python")

txt = r_23_package.receive_message.receive()

print (txt)