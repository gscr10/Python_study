# 参数名前加* 接受元组，加** 接收字典
def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


demo(1)
demo(1, 2, 3, 4, 5, name="xiaoming", age="18")


def sum_numbers(*args):

    num = 0
    print(args)

    for n in args:
        num += n

    return num


result = sum_numbers(1, 2, 3, 5, 6)
print(result)


# #### 元组和字典的拆包 #####
def demo1(*args, **kwargs):

    print(args)
    print(kwargs)


# 元组、字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name":"xao", "age":"18"}

demo1(*gl_nums, **gl_dict)
