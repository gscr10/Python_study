# 内置函数
	# len()
	# del()
	# max()  对于字典只比较key
	# min()
	# 字典不能比较大小

# 切片
    # 字典不能进行切片
print([0,1,2,3,4][::-1])
print((0,1,2,3,4)[::-1])

# 运算符
print([1,2]*5)
print((1,2)*2)

print((1,2) + (3,4))
list = [0,0]
list.extend([3,4])
print(list)

    # append当成元素加入
list.append(0)
print(list)

list.append([11,11])
print(list)

list.append((12,12))
print(list)

    # 成员运算符 in ， not in
print(3 in [2,3])
print(1 in [2,3])
print("a" in {"a":12})  # 判断字典key

# 完整的for循环
for g_num in [1, 2, 3]:
	print(g_num)
	if g_num == 2:
		break
else:
	# 如果循环体内部使用break退出，则else下方不执行
	print("??")

print("end")

students = [
    {"name":"111"},
    {"name":"222"}
]


find_name = "222"

for stu in students:
    print(stu)

    if stu["name"] == find_name:
        print("find  %s " % find_name)
        # 如果已经知道到应该退出循环
        break
else:
    print("not find")

print("end")

