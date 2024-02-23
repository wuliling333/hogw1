from random import randint
# 赢的次数
play_v=0
bot_v=0
for _ in rangr(3):
    play=int(input("请输入一个1-6的数字:"))
    bot=randint(1,6)
    if play==bot:
        print(f"点数相同,平局")
    elif play > bot:
        play_v+=1
        # print(f"玩家{play}点,电脑{bot}点,玩家赢")
    else:
        bot_v+=1
        # print(f"玩家{play}点,电脑{bot}点,机器人赢")
    if play_v>bot_v:
        print(f"玩家{play_v}次,电脑{bot_v}次,玩家赢")


