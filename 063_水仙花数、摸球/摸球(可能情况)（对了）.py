# 3 red balls ,3 yellow balls, 6 green balls, choose 8 from the 12 balls

for i in range(0,4):
    for j in range(0,4):
        for k in range(0,7):
            if (i + j + k) == 8:
                print("红球:{0}个".format(i),end="；")
                print("黄球:{0}个".format(j),end="；")
                print("绿球:{0}个".format(k))
                print("* " * 10)
