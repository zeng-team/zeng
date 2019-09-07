# class Women:
#     def __int__(self,name):
#         self.name = name
#         self.__age = 18
#     def __secret(self):
#         print("%s的年龄是%d" %(self.name,self.__age))
# xiaofang = Women("xiaofang")
# # 私有属性 外部不能直接访问
# # print(xiaofang.__age)
#
# # 私有方法 外部不能直接访问
# # xiaofang.__age
#
# # 伪私有属性 外部不能直接访问
# print(xiaofang._Women__age)
#
# # 伪私有方法 外部不能直接访问
# xiaofang._Women__secret()
#
#



class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test(self):
        print("私有方法%d %d"%(self.num1,self.__num2))
    def test(self):
        print("父类的公有方法%d"% self.__num2)
        self.__test()

class B(A):
    def demo(self):
        # 在子类的对象方法中 ，不能访问父类的私有属性
        # print("访问父类的私有属性%d" %self.__num2)
        # 在子类的对象中 ，不能调用父类的私有方法
        # self.__test()

        # 访问父类的公有属性
        print("子类方法%d" %self.num1)
        # 调用父类的公有方法
        self.test()
        pass
b = B()
print(b)

b.demo()
# 在外界访问公有属性和方法
# b.demo()
# print(b.num1)
# 在外界不能直接访问对象的私有属性和方法
# print(b.__num2)
# b.__test()