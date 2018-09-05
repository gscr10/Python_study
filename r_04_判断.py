age = 60

# if else 与其缩进部分是一个完整的代码块
# 逻辑运算   与：and   或：or   非：not 
# elif  多个条件，平级判断
# if嵌套 

if int(age) >= 18:
	print("成年了")
	if int(age) > 50:
		print("成年,且老了")
else:
	print("未成年")

# 石头剪刀布游戏
import random
player = int(input("请出拳  石头1/  剪刀2/  布3："))
computer = random.randint(1,3)  # 导入随机数
print("玩家出的是%d  ----   电脑出的是%d " % (player,computer))

# 增加一对扩号可以换行，八个空格缩进
if ((player == 1 and computer == 2) 
		or (player == 2 and computer == 3) 
		or (player == 3 and computer == 1)):  
	
	print("玩家胜利！")

elif ((player == 1 and computer == 1) 
		or (player == 2 and computer == 2) 
		or (player == 3 and computer == 3)): 
	
	print("平局了！")

else:
	print("电脑胜利！")
