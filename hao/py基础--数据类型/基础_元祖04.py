# -*- coding: utf-8 -*-
is_tuple = ("张三",18,1.75)

print(is_tuple[1])

print(is_tuple.count("张三"))

print(" %s  年龄%d  身高 %.2f" %is_tuple)
# len统计数据个数
print(len(is_tuple))


# 循环不常用
for my_dev in is_tuple:
    print(my_dev)
