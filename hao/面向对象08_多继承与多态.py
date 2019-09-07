# 多继承

# 开发时，尽量避免  父类之间存在属性和方法同名

# 新式类  以“object“为基类的类
# 经典类  不以"object"为基类的类
# 新式类和经典类 在多继承时，会影响到方法的搜索
class A():
    def test(self):
        print("A// test方法")
    def demo(self):
        print("B// demo方法")
class B:
    def test(self):
        print("A** test方法")
    def demo(self):
        print("B** demo方法")

class C(A,B):
# class C(B,A):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


c = C()
c.test()
c.demo()



# 多态
class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s蹦蹦跳跳。。" %self.name)
class XiaoTianQuan(Dog):
    def game(self):
        print("%s飞阿飞！！" %self.name)

class Person(object):
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s和%s玩耍。。"%(self.name,self.name))

wangcai = Dog("旺财")
xiaoming = Person("小明")
xiaoming.game_with_dog(wangcai)
