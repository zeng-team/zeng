# 在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量
def demo(num,num_list):
    print("函数内部的代码")
    num = 100 # 函数内部的赋值
    num_list = [1,2,3]
    print(num)
    print(num_list)
    print("函数执行完成")
gl_num = 80
gl_list = [4,5,6]
demo(gl_num,gl_list)
print(gl_num)
print(gl_list)
# 在函数内部使用方法修改可变参数会影响外部实参
def demo1(num_lsit):
    print("内部代码")
    num_lsit.append(9)
    print(num_lsit)
    print("执行完成")
gl_list1 = [1,2,3]
demo1(gl_list1)
print(gl_list1)


def demo2(num,num_list):
    print("函数开始")
    num += num
    # 列表变量使用 += 不会做相加再赋值的操作
    #
    # num_list = num_list + num_list
    # 本质上是在调用列表的 extend方法
    # num_list += num_list
    num_list.extend(num_list)
    print(num)
    print(num_list)
    print("函数结束")
gl_num1 = 6
gl_list2 = [1,2,3]
demo2(gl_num1,gl_list2)
print(gl_num1)
print(gl_list2)