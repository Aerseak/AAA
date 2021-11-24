'''
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，“猜小了”
起始金额为5000，猜对一次给300，猜错扣除100，猜错15次结束
'''
import random
#生成随机数
money=5000
i=0
while True:
    Value = random.randint(1,20)
    num=input("请输入一个数：")
    num=int(num)
    print(Value)
    if num == Value:
        print("你赢了")
        money+=300
    elif num>Value:
        print("猜大了")
        i+=1
        money-=100
    else:
        print("猜小了")
        i+=1
        money-=100
    if i==15:
        print("你输了")
        break
    print("总钱数：")
    print(money)