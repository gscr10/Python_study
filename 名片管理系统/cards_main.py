#! C:\Python37\python.exe

import cards_tools

# 无线循环，特定条件退出循环
while True:
    # 显示菜单
    cards_tools.show_menu()

    action_str =  input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3 针对名片操作
    if action_str in ["1","2","3"]:

        # 新增
        if action_str == "1":
            cards_tools.new_card()

        # 显示
        if action_str == "2":
            cards_tools.show_all()

        # 查询
        if action_str == "3":
            cards_tools.find_card()



    # 0 退出系统
    elif action_str == "0":
        # 如果在开发程序时不希望立刻编写分支代码
        # pass关键字表示一个占位符，不执行任何操作
        print("程序已退出")
        break

    # 其他内容报错
    else:
        print("输入有误，请重新输入")