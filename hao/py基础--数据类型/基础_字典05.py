# -*- coding: utf-8 -*-
in_tadi = {"name": "小明",
           "age": 17,
           "eight": 56}
in_que = {"height": 1.78}
# len统计数据的个数
print len(in_tadi)
# 查找值
print in_tadi["name"]
# 修改数据
in_tadi["age"] = 18
# pop删除单个数据
in_tadi.pop("eight")
# update合并数据
in_tadi.update(in_que)
# clear删除所有数据
# in_tadi.clear()
print in_tadi

# 循环遍历
for my_dev in in_tadi:
    print "%s - %s" % (my_dev,in_tadi[my_dev])

# 字典和列表组合
in_tabuo = [
    {"name": "张三",
     "age": "18",
     "height": "1.78"},
    {"name": "王五",
     "age": "20",
     "height": "1.73"}
]
for my_dev in in_tabuo:
    print my_dev