import random
import pymysql
from link import select
from link import update

con = pymysql.connect(host="localhost",user="root",password="",database="中国工商银行帐户管理库")
print("==================")
print("|   中国工商银行|   ")
print("==================")
print("|1、开户          |")
print("|2、存钱          |")
print("|3、取钱          |")
print("|4、转账          |")
print("|5、查询          |")
print("|6、退出          |")
print("==================")

bank={}

def useradd():
    account=random.randint(10000000,99999999)
    username=input("请输入您的姓名：")
    password=input("请输入您的密码：")
    country=input("\t\t请输入您的国家：")
    province=input("\t\t请输入您的省份：")
    street=input("\t\t请输入您的街道：")
    door=input("\t\t请输入您的门牌号：")
    money=0
    gift=bankadd(account,username,password,country,province,street,door,money)
    if gift == "1":
        print("开户成功")
        info = '''
                    ------工商银行------
                    1、账号：%s
                    2、姓名：%s
                    3、密码：******
                    4、国家：%s
                    5、省份：%s
                    6、街道：%s
                    7、门牌：%s
                    8、余额：%s
        '''
        print(info % (account,username,country,province,street,door,money))
    elif gift == "2":
        print("该账户名已被占用，请输入其他的账户名！")
    elif gift == "3":
        print("该数据库已满，请联系客服进行维修，给您带来不便，非常抱歉！")

def bankadd(account,username,password,country,province,street,door,money):
    sql = "select * from addition where username = %s"
    param = [username]
    data = select(sql,param)
    if len(data) > 0:
        return "2"
    sql1 = "select count(*) from addition"
    param1 = []
    data1 = select(sql1,param1)
    if data1[0][0] >= 100:
        return "3"
    sql2 = "insert into addition values(%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,username,password,country,province,street,door,money]
    update(sql2,param2)
    return "1"


#存钱
def accessadd():
    account = input("请输入帐户：")
    account = int(account)
    cq = input("请输入存款金额：")
    cq = int(cq)
    ba = bank_access(account,cq)
    if ba == True:
        print("存入成功")
    else:
        print("存钱失败！")

def bank_access(account,cq):
    sql = "select * from addition where account = %s"
    param = [account]
    data = select(sql, param)
    if len(data) > 0:
        sql1 = "update addition set money = money + %s where account = %s"
        param1 = [cq,account]
        update(sql1,param1)
        return True
    else:
        return False

#取钱
def moneyreduce():
    account = input("请输入帐户：")
    account = int(account)
    qc = input("请输入提取金额：")
    qc = int(qc)
    password = input("请输入密码：")
    br = bank_reduce(account,qc,password)
    if br == 0:
        print("取钱成功")
    elif br == 1:
        print("账号不存在")
    elif br == 2:
        print("密码错误")
    elif br == 3:
        print("钱不够")

def bank_reduce(account,qc,password):
    sql = "select * from addition where account = %s"
    param = [account]
    data = [sql,param]
    if len(data) > 0:
        sql1 = "select * from addition where account = %s and password = %s"
        param1 = [account,password]
        data1 = [sql1,param1]
        if len(data1) > 0:
            sql2 = "select * from addition where account = %s and money > %s"
            param2 = [account,qc]
            data2 = [sql2,param2]
            if len(data2) > 0:
                sql3 = "update addition set money = money - %s where account = %s"
                param3 = [qc,account]
                update(sql3,param3)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

#转账
def zhuanzhang():
    account = input("请转出输入帐号：")
    account = int(account)
    accountB = input("请输入转入帐号：")
    accountB = int(accountB)
    je = input("请输入转出金额：")
    je = int(je)
    password = input("\t请输入密码：")
    bs = bank_show(account,accountB,je,password)
    if bs == 0:
        print("转账成功！")
    elif bs == 1:
        print("转出或转入帐户不存在，请仔细检查输入的帐号")
    elif bs == 2:
        print("密码错误！！！")
    elif bs == 3:
        print("转出帐户的余额不足！")

def bank_show(account,accountB,je,password):
    sql = "select * from addition where account = %s and accountB = %s"
    param = [account,accountB]
    data = [sql,param]
    if len(data) > 0:
        sql1 = "select * from addition where account = %s and password = %s"
        param1 = [account,password]
        data1 = [sql1,param1]
        if len(data1) > 0:
            sql2 = "select * from addition where account = %s and money > %s"
            param2 = [account,je]
            data2 = [sql2,param2]
            if len(data2) > 0:
                sql3 = "update addition set money = money - %s where account = %s"
                param3 = [je,account]
                update(sql3,param3)
                sql4 = "update addition set money = money + %s where account = %s"
                param4 = [je, accountB]
                update(sql4, param4)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

#查询
def i():
    account = input("请输入您的帐号：")
    account = int(account)
    password = input("请输入您的密码：")
    o = bank_i(account,password)
    if o == 0:
        sql = "select *from addition where account = %s "
        param = [account]
        h = select(sql,param)
        print(h)
    elif o == 1:
        print("帐号错误！")
    elif o == 2:
        print("密码错误！")

def bank_i(account,password):
    sql = "select * from addition where account = %s"
    param = [account]
    data = [sql,param]
    if len(data) > 0:
        sql1 = "select * from addition where password = %s"
        param1 = [password]
        data1 = [sql1, param1]
        if len(data1) > 0:
            return 0
        else:
            return 2
    else:
        return 1


while True:
    box=input("请输入业务的编号：")
    if box == "1":
        print("1、开户")
        useradd()
    elif box == "2":
        print("2、存钱")
        accessadd()
    elif box == "3":
        print("3、取钱")
        moneyreduce()
    elif box == "4":
        print("4、转账")
        zhuanzhang()
    elif box == "5":
        print("5、查询")
        i()
    elif box == "6":
        print("Buy!Buy!")
        break