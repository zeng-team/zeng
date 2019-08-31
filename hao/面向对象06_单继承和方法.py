class Anime():
    def eat(self):
        print("chi")
    def run(self):
        print("pao")
    def sleep(self):
        print("shui")
class Dog(Anime):
    def bark(self):
        print("wang")
class xiaotianquan(Dog):
    def fly(self):
        print("fei")
    # 覆盖父类方法  重写
    # 在调用时 只会调用子类 而不会调用父类
    def bark(self):
        # 针对子类特有的需求 编写代码
        print("wowowo")
        # 使用super().  调用原本在父类中封装的方法
        super().bark()

xtq = xiaotianquan()
xtq.run()
xtq.bark()