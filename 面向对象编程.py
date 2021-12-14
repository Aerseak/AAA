import time

#空调
# class Air:
#     __brand = ""
#     __price = 0.0
#
#     def setBarand(self,brand):
#         if brand != "三菱重工" and brand != "格力" and brand != "美的" and brand != "海尔":
#             print("非常抱歉！本系统暂无此品牌空调。。。。。。")
#         else:
#             self.__brand = brand
#     def getBarand(self):
#         return self.__brand
#
#     def setPrice(self,price):
#         if price > 0:
#                 self.__price = price
#         else:
#             print("非法输入!!!")
#     def getPrice(self):
#         return self.__price
#
#
#
#     def state(self):
#         print("空调开机了...")
#
#     def shut(self,shi):
#         print("空调将在",shi,"秒后自动关闭...")
#         for i in range(shi):
#             print(".")
#             time.sleep(1)
#         print("空调关机完毕！")
#
#     def summary(self):
#         print("空调品牌：",self.__brand,"\t空调价格：",self.__price)
#
#
#
# A = Air()
# A.setBarand("格力")
# A.setPrice(356.6)
#
# A.state()
# A.shut(4)
# A.summary()



#学生
# class student:
#     __studname = ""
#     __age = 0
#
#
#     def setStudname(self,studname):
#         if studname == "":
#             print("姓名不为空！！！")
#         else:
#             self.__studname = studname
#     def getStudname(self):
#         return self.__studname
#
#     def setAge(self,age):
#         if age <= 0 or age > 120:
#             print("您的年龄不真实！！！")
#         else:
#             self.__age = age
#     def getAge(self):
#         return self.__age
#
#     def introduce(self):
#         print("大家好，我叫",self.__studname,"，今年",self.__age,"了。")
#
#     def classmate(self,Aname,Aage):
#         if Aage > 0 and self.__age > 0:
#             if Aage > self.__age:
#                 print("我叫", Aname, "，今年", Aage, "岁了,", self.__studname, "是我的同桌")
#                 print("我比他大",Aage-self.__age,"岁！")
#             elif Aage < self.__age:
#                 print("我叫", Aname, "，今年", Aage, "岁了,", self.__studname, "是我的同桌")
#                 print("我比他小",self.__age-Aage,"岁...")
#             elif Aage == self.__age:
#                 print("我叫", Aname, "，今年", Aage, "岁了,", self.__studname, "是我的同桌")
#                 print("我和他一样大！")
#         else:
#             print("你怕不是有啥大病？")
#
# s = student()
#
# s.setStudname("Aerseak")
# s.setAge(19)
#
# s.introduce()
# s.classmate(
# Aname = str(input("路人甲的姓名:")),
# Aage = int(input("路人甲的年龄:"))
# )



class phone:
    __name = ""#姓名
    __sex = ""#性别
    __age =0#年龄
    __gambit = 0#话费
    __conduct = ""#品牌
    __battery = 0#电池
    __screen = ""#屏幕
    __time = 0#时长
    __integral = 0#积分

    def setName(self,name):
        if name == "":
            print("姓名不为空！")
        else:
            self.__name = name
    def getName(self):
        return self.__name

    def setSex(self,sex):
        if sex == "":
            print("性别不为空！")
        elif sex == "男" or sex == "女":
            self.__sex = sex
        else:
            print("禁止胡乱填写性别！")
    def getSex(self):
        return self.__sex

    def setAge(self,age):
        if age <= 0 or age > 120:
            print("您的年龄不真实！！！")
        else:
            self.__age = age
    def getAge(self):
            return self.__age

    def setGambit(self,gambit):
        self.__gambit = gambit
    def getGambit(self):
        return self.__gambit

    def setConduct(self,conduct):
        if conduct == "":
            print("品牌不为空！")
        else:
            self.__conduct = conduct
    def getConduct(self):
        return self.__conduct

    def setBattery(self,battery):
        if battery <= 0:
            print("您确定这是电池吗？")
        else:
            self.__conduct = battery
    def getBattery(self):
        return self.__battery

    def setScreen(self,screen):
        self.__screen = screen
    def getScreen(self):
        return self.__screen

    def setTime(self,time):
        if time <= 0:
            print("您确定这时间是正确的吗？")
        else:
            self.__time = time
    def getTime(self):
        return self.__time

    def setIntegral(self,intearal):
        if intearal <= 0:
            print("您确定这积分是正确的吗？")
        else:
            self.__integral = intearal
    def getIntegral(self):
        return self.__integral




    def message(self,nameB,news):
        if nameB == "":
            print("您确定有这么一个人吗？")
        else:
            if news == "":
                print("您确定这是您想说的话吗？？？")
            else:
                print("发信息给：",nameB)
                print("\t",news)
    def telephone(self,dh,sj=""):
        if dh == "" and sj == "":
            print("电话不为空！")
        else:
            sj = int(sj)
            if sj <= 0:
                print("通话时长输入错误！")
            elif sj >= 0 and sj< 10:
                if sj*15 <= self.__integral:
                    self.__integral -= sj*15
                    print("时长*15,目前还剩",self.__integral,"积分")
                    print("当前帐户余额：",self.__gambit)
                else:
                    print("积分不足，本次通话将使用话费通话！")
                    if sj*1 <= self.__gambit:
                        self.__gambit =self.__gambit-sj*1
                        print(sj*1)
                        print("时长*1,目前还剩", self.__gambit, "话费")
                    else:
                        print("话费不足，请前往当地地区营业厅进行话费充值！")
            elif sj >= 10 and sj < 20:
                if sj*15 <= self.__integral:
                    self.__integral -= sj*39
                    print("时长*39,目前还剩", self.__integral, "积分")
                else:
                    print("积分不足，本次通话将使用话费通话！")
                    if sj*0.8 <= self.__gambit:
                        self.__gambit -= sj*0.8
                        print("时长*0.8,目前还剩", self.__gambit, "话费")
                    else:
                        print("话费不足，请前往当地地区营业厅进行话费充值！")
            elif sj >= 20:
                if sj*48 <= self.__integral:
                    self.__integral -= sj*48
                    print("时长*48,目前还剩", self.__integral, "积分")
                else:
                    print("积分不足，本次通话将使用话费通话！")
                    if sj*0.65 <= self.__gambit:
                        self.__gambit -= sj*0.65
                        print("时长*0.65,目前还剩", self.__gambit, "话费")
                    else:
                        print("话费不足，请前往当地地区营业厅进行话费充值！")
            else:
                print("别瞎闹！！！")

p = phone()

p.setName("Aerseak")
p.setSex("男")
p.setAge(19)
p.setGambit(100)
p.setConduct("OPPO")
p.setBattery(5000)
p.setScreen("1920*1080")
p.setTime(25)
p.setIntegral(100)



p.message(
    nameB=input("接收方："),
    news=input("请输入想发送的信息：")

)

# while True:
p.telephone(
    dh = input("请输入呼叫电话："),
    sj = input("请输入通话时长：")
)






























