# coding=utf-8

# 模块 每一个独立的源文件
# 模块名就是一个标识符，不能以数字开头


#import t_test1

# 使用from import 局部导入,导入后可直接通过工具名使用
# 若从不同模块中导入同名工具，后会覆盖前
# 若有冲突可用as起一个别名
from t_test1 import Dog as DDog

# 导入时使用别名,大驼峰命名法
import t_test2 as TsT2


# from import * 也可将所有工具导入，不推荐使用

# t_test1.say_hello()
TsT2.say_hello()

dog = DDog()
cat = TsT2.Cat()

print(dog)
print(cat)



# 模块的搜索顺序

import random

rand = random.randint(0, 10)
# 若本地文件中也存在random.py的文件，则无法正常使用
print(rand)

# __file__可以查看当前工具的文正路径
print(random.__file__)

# 当一个文件被导入时，所有未缩进的代码都会被执行一遍
# 直接执行的代码不是向外界提供个工具

# __name__属性
# 如果直接执行模块，返回__main__

"""
在编写的模块中的进行，进行测试功能的代码
测试代码不会再被调用时执行

def main():
    pass

if __name__ == "__main":
    main()


"""
