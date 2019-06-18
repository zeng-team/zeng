gl_list = [6,4,3,9]
# 默认按照升序排序
# gl_list.sort()
# 如果需要降序排序，需要执行reverse参数
gl_list.sort(reverse=True)
print(gl_list)


def print_info(name,gender=True):# 必须保证带有默认值的缺省参数在参数列表的末尾
    """

    :param name:班上姓名
    :param gender:Ture男生 False女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s是%s"%(name,gender_text))
# 假设男生居多
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值
print_info("小明") # 默认Ture 可以省略
print_info("老王")
print_info("小妹",False)
