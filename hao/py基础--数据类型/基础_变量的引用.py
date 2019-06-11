def variable(num):
    print("在函数内部%d对应的内存地址是%d"%(num,id(num)))

    result = "hello"
    print("函数返回数据的内存地址是%d" %id(result))

    # 将字符串变量返回，返回的是数据的引用，而不是数据本身
    return result

# 1定义一个变量
a = 10
# 数据的地址本质就是一个数字
print("变量a所在的内存地址是%d"% id(a))
# 2.调用函数，本质上传递的是实参保存数据的引用，而不是实参保存的数据
# 如果函数有返回值，但是没有定义变量接收
# 程序不会报错，但是无法获得返回结果
r = variable(a)

print("%s的内存地址是%d" %(r,id(r)))