def ctf(cel):
    fah = cel * 1.8 + 32
    return fah

def ftc(fah):
    cel = (fah - 32) / 1.8
    return cel

# 测试
def test():
    print("测试，0 摄氏度 = %.3f 华氏度" %ctf(0))
    print("测试，0 华氏度 = %.3f 摄氏度" %ftc(0))


if __name__ == "__main__":
    test()
