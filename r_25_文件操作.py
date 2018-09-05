# 文件操作

# 1个函数，3个方法
# 打开文件  open
file = open("test.txt", "a+")

"""
r   只读  指针放在开头  默认模式  文件不存在，抛出异常
w   只写  文件存在，覆盖  不存在，创建新文件
a   追加  文件存在，指针放在结尾  不存在，创建新文件
r+  读写  指针放在开头  文件不存在，抛出异常
w+  读写  文件存在，覆盖  不存在，创建新文件
a+  读写  文件存在，指针放在结尾  不存在，创建新文件

"""


# 读写文件  read write
file.write("hello python")

txt = file.read()
# 执行read后文件指针会移动到文件末尾
print(txt)

# 关闭文件  close
file.close()



# readline方法
# 一次读取一行
file = open("test.txt")

while True:
    text = file.readline()

    if not text:
        break

    print(text, end="")

file.close()



# 小文件的复制
# 1.打开文件
file_read = open("test.txt")
file_wirte = open("test_smile.txt", "w")

# 读写
text = file_read.read()
file_wirte.write(text)


# 关闭文件
file_read.close()
file_wirte.close()



# 大文件的复制
# 1.打开文件
file_read = open("test.txt")
file_wirte = open("test_big.txt", "w")

# 读写
while True:

    # 读取一行内容
    text = file_read.readline()

    # 判断是否读取到内容
    if not text:
        break

    file_wirte.write(text)


# 关闭文件
file_read.close()
file_wirte.close()