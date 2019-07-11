# 初始化方法
class Cat:
    def __init__(self,new_name):
        print("初始化方法")
        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name
    # 对象被从内存中销毁前，会被自动调用
    def __del__(self):
        print("%s去了"% self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫：%s" % self.name
    def eat(self):
        print("%s爱吃鱼"%self.name)

# 使用类名()创建对象的时候,会自动调用初始化方法__init__
tom = Cat("Tom")
tom.eat()
print(tom)

# lazy_cat = Cat("懒猫")
# lazy_cat.eat()