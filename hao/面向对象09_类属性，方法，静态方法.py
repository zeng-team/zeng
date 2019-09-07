# 类属性
class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    def __init__(self,name):
        self.name = name
        # 让类属性的值+1
        Tool.count += 1
# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("钳子")
tool3 = Tool("榔头")
# 输出工具对象的总数
print(Tool.count)


# 类方法
class Tool1(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    # 类方法需要用修饰器@classmethod来标识，表示这是一个类方法
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量%d" % cls.count)

    def __init__(self,name):
        self.name = name
        # 让类属性的值+1
        Tool1.count += 1

tool4 = Tool1("斧头")
tool5 = Tool1("钳子")
Tool1.show_tool_count()

# 静态方法
class Dog(object):
    # 静态方法需要用修饰器@staticmethod来标识，表示这是一个静态方法
    @staticmethod
    def run():
        print("小狗在跑。。")
# 通过类名，调用静态方法
Dog.run()