# 多个返回值
def measure():
    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")
    # 元祖可以包含多个数据，因此可以使用元祖让函数一次返回多个值
    # 如果函数返回的类型是元祖，小括号可以省略
    # return (temp,wetness)
    return temp,wetness
# 输出元祖类型
result = measure()
print(result)
# 需要单独处理数据  ————不方便
print(result[0])
print(result[1])
# 如果函数返回的类型是元祖，同时希望单独的处理元祖中的元素
# 可以使用多个变量，一次接受函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数应该和元祖中元素个数保持一致
gl_temp,gl_wetness = measure()
print(gl_temp)
print(gl_wetness)

# 交换数字
a = 6
b = 100
# 解法一：使用其他变量
# c = a
# a = b
# b = c
# 解法二：不使用其他变量
# a = a+b
# b = a-b
# a = a-b
# 解法三：python专有
# a,b = (b,a)
# 提示：等号右边是一个元祖，只是把小括号省略了
a,b = b,a
print(a)
print(b)