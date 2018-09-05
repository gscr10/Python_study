# while循环
sum = 0
j = 0  # 计数一般从0开始
while (j <= 100):
	if (j%2 == 0):
		print(j)
		sum += j
	j += 1

print("求和=%d " % sum)

# break   continue
i = 0
while  i<= 10:
	if i == 6:
		print("6666")
		i += 1    # 若使用continue前不处理计数器就会死循环
		continue  
	if i == 9:
		break
	print(i)
	i += 1

#print不换行,使用end=""
print("afdsafd----", end="")  
print("dfad")

row = 1
while row <= 5:
	
	col = 1
	while col <= row:
		# print("第%d列" % col, end="")
		print("*",end="")
		col += 1
	
	print("  --第%d行" % row)
	row += 1

def multiple_table():

	# 9*9乘法表
	n1 = 1
	result = 0
	while n1 <= 9:
		n2 = 1
		while n2 <= n1:
			result = n1 * n2
			print("%d * %d = %d" % (n2,n1,result), end="\t")
			n2 += 1
		n1 += 1
		print("")

# 转义字符: 
# \\ 反斜杠 \' 单引号 \" 双引号  \n 换行 \t 横向制表符 \r 回车  


	