class Game(object):
    top_score = 0
    def __init__(self,player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("游戏帮助信息。。。。")

    @classmethod
    def show_top_score(cls):
        print("历史记录%d" % cls.top_score)

    def start_game(self):
        print("%s游戏开始。。" % self.player_name)

# 查看游戏信息
Game.show_help()
# 查看历史高分
Game.show_top_score()
# 创建游戏对象
game = Game("小明")
game.start_game()