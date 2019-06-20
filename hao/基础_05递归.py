# 递归：一个函数内部调用自己也可以调用其他函数
# 当瞒足一个条件时，函数不再执行，通常被称为递归的出口，否则会死循环
def num_sumber(num):
    print(num)
    # 设置递归的出口，满足一定条件后不再执行
    if num == 1:
        return
    # 自己调用自己
    num_sumber(num - 1)
num_sumber(3)

# 递归数字累加
def sum_numbers1(num):
    # 出口
    if num == 1:
        return 1
    # 数字累加 num+(1...num-1)
    # 假设sum_numbers1 能够正确的处理1...num-1
    temp = sum_numbers1(num - 1)
    # 两个数字的相加
    return num + temp
result1 = sum_numbers1(100)
print(result1)