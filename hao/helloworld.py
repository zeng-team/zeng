# dol = 1
# while dol <= 9:
#     des = 1
#     while des <= dol:
#         print("%d * %d = %d" %(des,dol,dol*des),end="\t")
#         des += 1
#     print("")
#     dol += 1

def sum():
    import random
    player = int(input("输入数字 剪刀(1)石头(2)布(3)："))
    computer = random.randint(1,3)
    print("你输入的数：%d" %player)
    print("电脑输入的数：%d" %computer)
    if ((player == 1 and computer ==3)
        or (player == 2 and computer == 1)
            or (player == 3 and computer ==2)):
        print("你赢了!")
    elif player == computer:
        print("平局!")
    else:
        print("你输了！")
