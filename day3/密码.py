a = 1
while a<=3:
    add=input("请输入你的账号：")
    w=input("请输入你的密码：")
    if add == "root" and w == "admin":
        print("登录成功！")
        break
    else:
        a += 1
        print("登录失败！")
print("锁定中")
