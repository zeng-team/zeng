# 封装案例————属性是可以另一个类创建的对象

class Gun:
    def __init__(self,model):
        # 1枪的型号
        self.model = model
        # 2子弹的数量
        self.bullet_count = 0
    def add_bullet(self,count):
        self.bullet_count += count
    def shoot(self):
        # 1判断子弹数量
        if self.bullet_count <= 0:
            print("%s没有子弹了。。。" %self.model)
            return
        # 2发射子弹,-1
        self.bullet_count -= 1
        # 3提示发射信息
        print("%s 突突突...%d" %(self.model,self.bullet_count))

class Soldier:
    def __init__(self, name):
        # 1、士兵名
        self.name = name
        # 2、枪 -没有枪
        self.gun = None
    def fire(self):
        # 1 判断是否有枪
        # is是判断两个标识符是不是引用同一个对象
        # is not是判断两个标识符是不是引用不同对象
        # ”is“用于判断两个变量引用对象是否为同一个
        # “==”用于判断引用变量的值是否相等
        # if self.gun == None:
        if self.gun is None:
            print("%s还没有枪。。。"% self.name)
            return
        print("冲啊。。。%s" %self.name)
        # 2 装填子弹
        self.gun.add_bullet(50)
        # 3 发射
        self.gun.shoot()


ak47 = Gun("AK47")
#
# ak47.add_bullet(40)
# ak47.shoot()

zhangsan = Soldier("张三")

zhangsan.gun = ak47
zhangsan.fire()
print(zhangsan.gun)
