# "名词"类型属于"属性"
# "动词"类型属于"方法"
class Cat:
    def eat(self):
        # 哪一个对象调用的方法,self就是哪一个对象的引用
        print("%s爱吃鱼"%self.name)
    def drink(self):
        print("%s爱喝水"%self.name)
tom = Cat()
# 可以使用 .属性名   利用赋值语句就可以了
# 日常开发,不推荐在类的外部增加属性
tom.name = "Tom"
tom.eat()
tom.drink()
lazy_cat = Cat()
lazy_cat.name = "懒猫"
lazy_cat.drink()
lazy_cat.eat()