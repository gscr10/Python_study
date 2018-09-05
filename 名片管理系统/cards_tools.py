# 所有名片记录列表
card_list = []


def show_menu():
    """显示菜单"""

    print("*" * 50)
    print("欢迎使用【名片管理系统】 v1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""

    print("-" * 50)
    print("【功能】新增名片")
    print("")

    # 1.提示用户输入名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")
    # 2.使用用户输入信息建立名片字典
    card_dict = {"name":name_str,
                 "phone":phone_str,
                 "qq":qq_str,
                 "email":email_str}

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)

    # 4.提示添加成功
    print("名片 %s 添加成功" % name_str)


def show_all():
    """显示所有名片"""

    print("-" * 50)
    print("【功能】显示名片")
    print("")

    # 判断是否存在名片记录，如果没有，提示用户返回
    if len(card_list) == 0:
        print("没有名片，请添加")

        # 返回函数执行结果
        # 下方代码不会被执行
        # 若return后面没有任何内容，返回函数调用位置
        # 不返回任何结果
        return

    # 打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name, end="\t\t")

    print("")

    # 打印分割线
    print("=" * 50)

    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:

        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def find_card():
    """查询名片"""

    print("-" * 50)
    print("【功能】查询名片")
    print("")

    find_name = input("请输入需要查询的姓名：")

    if len(card_list) == 0:
        print("没有名片，请添加")
        return


    for card_dict in card_list:

        if card_dict["name"] == find_name:

            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")
            print("")

            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))

            print("-" * 50)

            # 对名片进行修改
            deal_card(card_dict)

            break
    else:
        print("没有找到%s" % find_name)


def deal_card(find_dict):
    """修改名片"""

    action_str = input("请选择你要进行的操作："
                       "[1].修改 [2].删除 [0].返回上级菜单")

    # 1.修改
    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"],
                                            "姓名【回车不修改】：")
        find_dict["phone"] = input_card_info(find_dict["phone"],
                                             "电话【回车不修改】：")
        find_dict["qq"] = input_card_info(find_dict["qq"],
                                          "QQ【回车不修改】：")
        find_dict["email"] = input_card_info(find_dict["email"],
                                             "邮箱【回车不修改】：")


        # deal_name = input("请输入新的姓名：【回车不修改】")
        # if deal_name == "\n":
        #     print("姓名没有修改")
        # else:
        #     find_dict["name"] = deal_name
        #
        # deal_phone = input("请输入新的电话：【回车不修改】")
        # if deal_phone == "\n":
        #     print("电话没有修改")
        # else:
        #     find_dict["phone"] = deal_phone
        #
        # deal_qq = input("请输入新的QQ：【回车不修改】")
        # if deal_qq == "\n":
        #     print("QQ没有修改")
        # else:
        #     find_dict["qq"] = deal_qq
        #
        # deal_email = input("请输入新的邮箱：【回车不修改】")
        # if deal_email == "\n":
        #     print("邮箱没有修改")
        # else:
        #     find_dict["email"] = deal_email

    # 2.删除
    elif action_str == "2":
        card_list.remove(find_dict)

        print("删除%s名片成功" % find_dict["name"])


def input_card_info(dict_value,tip_message):
    """判断是否修改信息
    :param dict_value: 名片字典原有值
    :param tip_message: 用户修改值
    :return: 返回值
    """
    # 1.提示用户输入信息
    result_str = input(tip_message)

    # 2.判断输入内容，若有则修改，没有则换回原值
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value











