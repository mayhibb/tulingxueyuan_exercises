# 第三次尝试
import random as r


class Turtle():
    def __init__(self):
        self.power = 100
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        re_x = 0
        re_y = 0
        # 当 0 < |re_x| + |re_y| <= 2,时是有效的数字,乌龟移动 1 or 2
        while (abs(re_x) + abs(re_y)) == 0 or (abs(re_x) + abs(re_y)) > 2:
            re_x = r.choice([-2, -1, 0, 1, 2])
            re_y = r.choice([-2, -1, 0, 1, 2])

        new_x = self.x + re_x
        if new_x < 0:
            self.x = 0 - (new_x - 0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        new_y = self.y + re_y
        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        self.power -= 1
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100


class Fish():
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        re_x = 0
        re_y = 0
        # 当 0 < |re_x| + |re_y| <= 1,时是有效的数字,鱼移动 1
        while (abs(re_x) + abs(re_y)) == 0 or (abs(re_x) + abs(re_y)) > 1:
            re_x = r.choice([-1, 0, 1])
            re_y = r.choice([-1, 0, 1])

        new_x = self.x + re_x
        if new_x < 0:
            self.x = 0 - (new_x - 0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        new_y = self.y + re_y
        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        return (self.x, self.y)


# 实例化1只乌龟和10条鱼
turtle = Turtle()
fish = []
for each in range(10):
    new_fish = Fish()
    fish.append(new_fish)

# 游戏的运行
while True:
    if not len(fish):
        print("鱼被吃完了，游戏结束。")
        break
    if not turtle.power:
        print("乌龟没有力气了，游戏结束。")
        break

    staps = turtle.move()
    for each_fish in fish[:]:
        if each_fish.move() == staps:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼被吃掉了")

