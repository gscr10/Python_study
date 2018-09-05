####### 列表  ######

name_list = ["aaaaaaa","bbb","ccc"]

# 取值
print(name_list[0])
# 取索引
print(name_list.index("ccc"))

# 修改，索引不能超出范围
name_list[0] = "aaa"
print(name_list)

# 增加
name_list.append("ddd")   # 末尾追加
name_list.insert(1,"b")   # 制定索引位置插入
temp_list = ["11","22","33"]
name_list.extend(temp_list)  # 其他列表内容追加当前列表尾
print(name_list)

# 删除
name_list.remove("b")   # 删除指定数据，重复的话删第一个
name_list.pop()   # 默认删除尾部数据
name_list.pop(3)  # 可以制定要删除位置的索引
temp_list.clear()  # 清空列表
print(name_list)
print(temp_list)

del name_list[0]  # 从内存中删除
print(name_list)

# 统计
list_len = len(name_list)   # 列表长度
print(list_len)

count = name_list.count("ccc")  # 某数据出现次数
print(count)

# 排序
name_list.sort()  # 升序
print(name_list)

name_list.sort(reverse=1)  # 降序
print(name_list)

name_list.reverse()   # 逆序
print(name_list)

# 循环遍历

for name in name_list:
	print(name)


######## 元组 tuple ########

# 元组的元素不能修改

info_tuple = ("ahngs", 19, 1.75,1.75)  # 可以存储不同数据类型
print(info_tuple[2]) 
empty_tuple = ()  # 空元组
single_tuple = (50,)  # 只有一个元素的元组

print(info_tuple[0])  # 取值
print(info_tuple.index(19))  # 取索引
print(info_tuple.count(1.75))  # 某元素重复次数
print(len(info_tuple))   # 计算元组长度

# 循环遍历
for item in info_tuple:
	print(item)  # 因保存元素格式不同，格式化输出不便

# 应用场景

# 格式化字符串
info = ("xiaoguo", 18, 1.75)
print("%s 的年龄是%d  身高是%.2f" % info)
info_str = "%s 的年龄是%d  身高是%.2f" % info
print(info_str)
print(type(info))
print(type(info_str))

# 元组和列表之间的转换
name_list_tuple = tuple(name_list)  # tuple() 列表转元组
print(type(name_list_tuple))
info_list = list(info)  # list() 元组转列表
print(type(info_list))


######### 字典  ##########

#值可以是任何数据类型，键只能是字符串、数字、元组
xiaoming_dict ={"height": 1.75,
				"age":14,
				"weight":55}

print(xiaoming_dict["height"])  # 取值
xiaoming_dict["age"] = 18   # key存在，增加
xiaoming_dict["height"] = 180  # key存在，修改
xiaoming_dict.pop("weight")   # 删除

print(len(xiaoming_dict))  # 统计key数量

temp = {"age": "18",
		"weight":"45.00"}
# .update()合并字典，若有相同key则覆盖 
xiaoming_dict.update(temp)  
temp.clear()  # 清空字典
print(temp)

# 循环遍历
for key in xiaoming_dict:
	print("%s -- %s" % (key, xiaoming_dict[key]))

# 应有场景
card_list = [
	{"name":"zhang",
	 "qq":"12344",
	 "phone":"111"},
	{"name":"wang",
	 "qq":"12355",
	 "phone":"1222"}
]
for card_info in card_list:
	print(card_info)


######### 字符串 ##########

str = "hello python"
print(str[3])
print(len(str))  # 计算长度
print(str.count("llo"))  # 子字符串的重复次数
print(str.index("on"))  # 子字符串的出现位置

# 字符串常用操作

# 判断类型
# 1.判断空白字符
space_str = "   \t\n\t"
print(space_str.isspace())   

# 2.判断是否只包含数字
	# 1>都不能判断小数
	# 2>.isdigit()可判断unicode 字符串 \u00b2 、(1)
	# 3>.isnumeric()可判断中文数字
num_str = "11"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

# 查找替换
	# 1.判断是否以指定的字符串开始
print(str.startswith("hello"))
	# 2.判断是否以制定的字符串结束
print(str.endswith("python"))
	# 3.查找指定的字符串,不存在返回-1
		# index同样可以查找指定子字符串在大字符串中的索引
		# index不存在报错
print(str.find("llo"))
print(str.find("ss"))
	# 4.替换字符串
		# replace方法执行后，会返回一个新的字符串
		# 不会修改原有字符串内容
print(str.replace("python","world"))
print(str)

# 文本对其
peom = ["dfasdfsda",
		"dfafd",
		"fsdafsd",
		"fdsfdgggg",
		"jkljl"]
for peom in peom:
	print("|%s|" % (peom.center(15, " ")))  # 居中
for peom in peom:
	print("|%s|" % (peom.ljust(15, " ")))  # 左
for peom in peom:
	print("|%s|" % (peom.rjust(15, " ")))  # 右

# 去掉空白字符
	# .strip()方法 .lstrip()去左  .rstrip()去右
peom2 = ["\t\ndfasdfsda",
		"dfafd",
		"fsdafsd\t\n",
		"fdsfdg    ggg     ",
		"jkljl"]
for peom2 in peom2:
	print("|%s|" % (peom2.strip().center(25, " "))) 

#拆分和连接
peom_str = "hfkdahfk\t  fasdf\n \t fasdfasd\t\t fsadfasda\t\n"
print(peom_str)
	# 1.拆分字符串
peom_list = peom_str.split()
print(peom_list)
	# 2.合并字符串
result = " --- ".join(peom_list)
print(result)

# 切片
num_s = "0123456789"
print(num_s[2:6])  # 2-5
print(num_s[2:])  # 2-结束
print(num_s[:6])  # 开始-5
print(num_s[:])   # 完成
print(num_s[::2])  # 从开始，每隔一个  
print(num_s[1::2])  # 从索引1，每隔一个 
print(num_s[2:-1])  # 从2- 末尾-1
print(num_s[-2:])   # 末尾2字符
print(num_s[::-1])  # 逆序
