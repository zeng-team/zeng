card_list = []


def show_menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    print("-" * 50)
    print("新增名片")
    # 提示输入信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入邮箱：")
    # 使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 把字典中的数据保存到列表中
    card_list.append(card_dict)
    print(card_list)
    # 提示添加成功
    print("添加%s的名片成功！" % name_str)


"""显示所有名片

:return: 判断是否有数据，如果没有返回函数调用的位置
"""


def show_all():
    print("-" * 50)
    print("显示所有名片")
    # 判断是否存在名片记录，如果没有返回
    if len(card_list) == 0:
        print("当前没有任何到名片记录，请使用新增功能添加名片！")
        # return可以返回一个函数的执行结果
        # 下方的代码不会执行
        # 如果return后面没有任何的内容，表示会返回到调用函数的位置，并且不返回任何的结果
        return
    # 表头显示
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="'\t\t")
    print("")
    print("=" * 50)
    # 显示名片内容
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入你要查询的名片：")
    # 输出搜索的名片
    for card_dict in card_list:
        # 判断字典中是否存在搜索的名字
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)  # card_dict 保存原有字典数据的参数
            break
    else:
        print("抱歉，没有找到%s" % find_name)


"""处理查找到的名片

:param find_dict: 查找到的名片
:return:返回调用函数位置
"""


def deal_card(find_dict):  # find_dict 保存新的数据参数
    print(find_dict)
    action_str = input("请选择要执行的操作 "
                       "【1】修改 【2】删除 【0】返回上级")
    if action_str == "1":
        find_dict["name"] = input_find_aict(find_dict["name"], "姓名:")
        find_dict["phone"] = input_find_aict(find_dict["phone"], "电话:")
        find_dict["qq"] = input_find_aict(find_dict["qq"], "QQ:")
        find_dict["email"] = input_find_aict(find_dict["email"], "邮箱:")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片")
    else:
        return find_dict


"""输入名片信息

    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容，就返回内容，否则返回字典中原有的值
"""


def input_find_aict(dict_value, tip_message):
    # 提示用户输入内容
    result_str = input(tip_message)
    # 针对用户输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value