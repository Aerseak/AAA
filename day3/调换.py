A = 56
B = 78
print("A=",A)
print("B=",B)
while True:
    n = input("请使用+或-来进行调换操作：")
    if n == "+" or n == "-":
        A,B = B,A
        print("A=",A)
        print("B=",B)
    else:
        print("......")