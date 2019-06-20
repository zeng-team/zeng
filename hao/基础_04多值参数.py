# 多值参数
# 定义支持多值参数的函数：在参数名前加个“*”可以接收元祖
#                    在参数名前加个“**”可以接收字典
# *args存放元祖参数， **kwargs存放字典参数
def demo5(num,*nums,**person):
    print(num)
    print(nums)
    print(person)
demo5(1,2,3,4,5,name="小明",age="18")

# 数字累加
def sum_numbers(*args):
    num = 0
    print(args)
    # 循环遍历
    for n in args:
        num += n
    return num
result = sum_numbers(1,2,3,4)
print(result)

# 字典和元祖的拆包
def deml1(*args,**kwargs):
    print(args)
    print(kwargs)

gl_nums = (1,2,3)
gl_dict = {"name": "小明", "age": 18}
# deml1(gl_nums,gl_dict)
# 拆包语法：简化元祖/字典变量的传递
deml1(*gl_nums,**gl_dict)