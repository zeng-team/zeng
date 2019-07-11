class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s,体重是%.2f公斤" %(self.name,self.weight)
    def eat(self):
        print("%s是吃货"% self.name)
    def run(self):
        print("%s爱跑步"% self.name)
        self.weight -= 2

xiaoming = Person("小明",65)
xiaoming.eat()
xiaoming.run()
print(xiaoming)
xiaomei = Person("小美",45)
xiaomei.run()
xiaomei.eat()
print(xiaomei)