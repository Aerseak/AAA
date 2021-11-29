for i in range(10):
    for a in range(0, 10 - i):
        print(end=" ")
    for b in range(10 - i, 10):
        print("*", end=" ")
    print("")