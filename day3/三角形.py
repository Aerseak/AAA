'''
请输入三个数
'''
i = 0
while i < 1:
    a, b, c = map(int, input("请输入三个值:").split(','))
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("等边三角形")
        elif a == c != b or a == b != c or b == c != a:
            print("等腰三角形")
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("直角三角形")
        else:
            print("普通三角形")
    else:
        print("无法构成三角形")
        break
