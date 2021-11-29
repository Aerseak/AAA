i=1
a = input("请输入值：")
if a.isdigit():
    a = int(a)
    while i <= a:
        b = 1
        while b <= i:
            print("%dx%d=%d"% (i,b,i*b),end=" ")
            b += 1
        print(" ")
        i += 1
else:
    print("......")