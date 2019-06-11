name = "小明"
dife = [
    {"name": "张三"},
    {"name": "李四"}
]
# name = "小明"
for new_dife in dife:
    print(new_dife)
    if name == new_dife["name"]:
        print("找到了 %s" % name)
        break
else:
    print("%s 不存在" % name)
print("结束")

# max最大值
# min最小值
# del删除变量
# cmp比较值
# “+”合并 字典不可用
# “*”重复 字典不可用
# in元素是否存在 都可用
# not in元素是否不存在 都可用