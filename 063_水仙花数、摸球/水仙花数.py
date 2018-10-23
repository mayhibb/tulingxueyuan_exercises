for i in range(100,1000):
    num = list(str(i))
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])

    if (a**3 + b**3 + c**3) == i:
        print(i)
