# class oldphone:
#     brand = ""
#
#
#     def setBrand(self,brand):
#         if brand == "":
#             print("无")
#         else:
#             self.brand = brand
#     def getBrand(self):
#         return self.brand
#
#
#     def one(self,Aphon):
#         print("正在给",Aphon,"打电话...")
#
#
# o = oldphone()
# o.setBrand("OPPO")
# o.one(19871207060)
#
#
#
# class newphone(oldphone):
#     pass
#
#     def two(self,Aphon):
#         print("语言拨号中...")
#         super().one(Aphon)
#         print("品牌为:",self.brand,"的手机很好用")
#
# o = newphone()
# o.setBrand("锤子")
# o.two("阿伟")





# class chef:
#     name =""
#     age = 0
#
#     def setName(self,name):
#         if name == "":
#             print("无名大侠？？？")
#         else:
#             self.name = name
#     def getName(self):
#         return self.name
#
#     def setAge(self,age):
#         if age <= 0 and age >= 120:
#             print("修仙呢？")
#         else:
#             self.age = age
#     def getAge(self):
#         return self.age
#
#
#     def rice(self):
#         print(self.name,"正在蒸饭！")
#
#
# class chefson(chef):
#     pass
#
#     def dish(self):
#         print(self.name,"正在炒菜！")
#
# class chefgrandson(chefson):
#     pass
#     def introduce(self):
#         print(self.name,"今年",self.age,"岁,是假面骑士！")
#     def rice(self):
#         print(self.name,"不会蒸饭！")#重写chef的方法
#     def dish(self):
#         print(self.name,"不会炒菜！")#重写chefson的方法
#
# C = chefgrandson()
# C.setName("欧茨")
# C.setAge(22)
# C.introduce()
# C.rice()
# C.dish()



class people:
    age = 0
    sex = ""
    name = ""

    def setAge(self,age):
        if age <=0 and age >120:
            print("哥几个，修仙讷？")
        else:
            self.age = age
    def getAge(self):
        return self.age

    def setSex(self,sex):
        if sex =="男" or sex == "女":
            self.sex = sex
        else:
            print("哥几个，去过泰国呀？")
    def getSex(self):
        return self.sex

    def setName(self,name):
        if name == "":
            print("哥几个，无名大侠吖？")
        else:
            self.name = name
    def getName(self):
        return self.name



class worker(people):
    pass

    def work(self):
        print(self.name,"性别:",self.sex,"今年",self.age,"岁，是打工楞。")

a = worker()
a.setName("芜湖")
a.setSex("男")
a.setAge(28)
a.work()


class student(people):
    pass
    number = ""#学号

    def setNumber(self,number):
        if number == "":
            print("请输入学号！！")
        else:
            self.number = number
    def getNumber(self):
        return self.number

    def learn(self):
        print("学号：",self.number,"姓名：",self.name,"年龄：",self.age,"性别：",self.sex,"每天会去图书馆看书学习")

    def dance(self):
        print("学号：", self.number, "姓名：", self.name, "年龄：", self.age, "性别：", self.sex, "每天会去舞蹈室学习跳舞")

b = student()
b.setNumber("205001064")
b.setName("竹溪")
b.setAge(19)
b.setSex("女")
b.learn()
b.dance()











