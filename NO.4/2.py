print('hello')
temp=input("不妨猜下我想的是那个数字：")
guess=int(temp)
while guess!=8:
    temp=input("猜错了，重新输入吧：")
    guess=int(temp)
    if guess==8:
        print("我靠这都猜到了")
        print("但是没奖励")
    else :
        if guess>8:
            print("大了大了")
        else:
            print("小了小了")

print("游戏结束")
