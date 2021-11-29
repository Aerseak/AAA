i = 9
while i >= 1:
    for j in range(1,i+1):
        print("  ",j,"x",i,"=",i*j,end="")
    i-= 1
    print()
