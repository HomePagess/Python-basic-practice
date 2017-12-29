import random
secret=random.randint(1,10)
print('hello')
temp=input("不妨猜下我想的是那个数字：")
guess=int(temp)
while guess!=secret:
    if guess>secret:
        temp=input("大了大了，重新输入吧：")
    else:
        temp=input("小了小了，重新输入吧：")
    guess=int(temp)
    if guess==secret:
        print("我靠这都猜到了")
        print("但是没奖励")
print("游戏结束")
