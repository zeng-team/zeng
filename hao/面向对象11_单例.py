# 单例:目的让类创建的对象，在系统中只有唯一的一个实例
# 每一次执行 类名() 返回的对象，内存地址是相同的

# __new__的作用
# 在内存中为对象分配空间
# 返回对象的引用
class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # # 创建对象是，new方法会被自动调用
        # print("分配空间。。")
        # # 为对象分配空间
        # instance = super().__new__(cls)
        # # 返回对象的引用
        # return  instance


        # 判断类属性是否是空对象
        if cls.instance is None:
            # 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象引用
        return cls.instance

    # 只调用一次初始化方法
    def __init__(self):
        # 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 如果没有执行过，在执行初始化动作
        print("播放初始。。")
        # 修改类属性的标记
        MusicPlayer.init_flag = True


# 创建播放器对象
player = MusicPlayer()
print(player)
player1 = MusicPlayer()
print(player1)
