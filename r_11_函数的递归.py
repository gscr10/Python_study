def sum_num(num):
    print(num)
    # 递归出口，当参数满足某个条件时，不在执行函数
    if num == 1:
        return

    # 自己调用自己
    sum_num(num - 1)


sum_num(3)

def sum(num):

    # 1. 出口
    if num == 1:
        return 1

    # 2.数字累加 num + （1... num-1）
    temp = sum(num - 1)
    return num + temp


result = sum(4)
print(result)
