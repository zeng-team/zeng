name_list = ["ps","ss","op"]
# 直接输出列表中相应位置的数
print(name_list[2])
# index索引，显示数据的位置,如果传递的数据不在列表中，程序会报错
print(name_list.index("ss"))
# 修改列表
name_list[2] = "cd"

# append末尾加数据
name_list.append("cba")
# insert在列表插入数据
name_list.insert(2,"bb")
# extend把另外的列表完整内容追加到列表末尾
temp = ["wu","li","ti"]
name_list.extend(temp)

# remove列表删除指定到数据
name_list.remove("ps")
# pop指定删除数据到索引
name_list.pop(2) # 默认删除末尾
# clear清空列表数据
name_list.clear()
# del 删除列表内容，也可将一个变量从内存中删除
# del name_list[3]
print(name_list)


list_name = ["xx","ss","bb","bb"]
# len统计列表元素的总数
pen = len(list_name)
print(pen)
# count 统计列表某数据出现的次数
count = list_name.count("bb")
print(count)


name_list=["p","t","c","r"]
name_lise=[8,1,6,3]
# sort 把数据以升序显示
# name_list.sort()
# name_lise.sort()

# reverse=True 把数据以降序显示
# name_list.sort(reverse=True)
# name_lise.sort(reverse=True)

# reverse 把列表数据以逆序显示
name_list.reverse()
name_lise.reverse()

print(name_list)
print(name_lise)

for my_word in name_list:
    print("输出单词%s" %my_word)