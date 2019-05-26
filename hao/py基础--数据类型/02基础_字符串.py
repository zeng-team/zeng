dife = "hello word"
print(len(dife))

# 判断是否以指定字符串开始
print(dife.startswith("hello"))

# 判断是否以指定字符串结束
print(dife.endswith("word"))

# 查找指定字符串  当find输入字符串不存在时输出-1
# 同index一样 当index输入字符串不存在时报错
print(dife.find("ll"))  # rfind 类似find 不过是从右边开始查找
print(dife.index("e"))  # rindex 类似index 是从右边开始查找

# 替换字符串
# 注意 ：不会修改原有字符串到内容
print(dife.replace("word", "python"))
print(dife)

# count数据的个数
print(dife.count("l"))



poem = ["登鹤雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:
#   print("|%s|" % poem_str.center(12,"　"))  #居中对齐
#  print("|%s|" % poem_str.ljust(12,"　"))  #向左对齐
#   print("|%s|" % poem_str.rjust(12, "　")) # 向右对齐

# strip方法可以去除字符串中的空白字符
    print("|%s|" % poem_str.strip().center(12,"　"))



# isspace判断空白字符 输出True
dife_str = " \t\r\n "
print(dife_str.isspace())

#判断字符串中是否只包含数字   不包含小数
sum_str = "3"
print(sum_str)
print(sum_str.isdecimal())
print(sum_str.isdigit())   # (1),\u00b2表示二次方
print(sum_str.isnumeric())  # 包含中文数字


poem_new = "登鹤雀楼\t\n王之涣\t白日依山尽\t\n黄河入海流\t\n欲穷千里目\t更上一层楼"
# 拆分字符串
print(poem_new.split())
# 合并字符串
print(" ".join(poem_new))