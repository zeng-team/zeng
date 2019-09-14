# 完整的异常捕获语法
try:
    num = int(input("输入整数:"))
    result = 8 / num
except ValueError:
    print("重新输入")
# except ZeroDivisionError:
#     print("不可以除以0")
# 捕获未知的异常
except Exception as reslut:
    print("未知异常 %s" %result)

else:
    print("正常运行")
finally:
    print("无论正常与否，都将运行")


# 异常的传递性
def demo1():
    num = int(input("输入整数:"))
def demo2():
    print(demo1())
# 为了代码的整洁性，可以在代码的主函数中添加异常捕获
try:
    print(demo2())
except Exception as result:
    print("未知异常 %s" %result)


# 主动抛出异常
def input_password():
    pwd = input("请输入密码:")
    # 判断密码长度 >= 8,返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 如果小于8 主动抛出异常
    print("主动抛出异常")
    # 创建异常对象
    ex = Exception("密码长度不够")
    # 主动抛出异常
    raise ex
try:
    print(input_password())
except Exception as result:
    print(result)