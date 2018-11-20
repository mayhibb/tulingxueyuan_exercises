import random as r

class Turtle():
    def __init__(self):
        self.name = "小甲鱼"

        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

        self.life = 100

        print('小甲鱼的诞生地',self.x,",",self.y)

    def turtle_move(self):
	# 移动一格或者两格
        new_x = self.x + r.choice([-2,-1,1,2])
        new_y = self.y + r.choice([-2,-1,1,2])

        if new_x < 0:
            self.x = 0 - ( new_x - 0 )
        elif new_x > 10:
            self.x = 10 - ( new_x - 10 )
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - ( new_y - 0 )
        elif new_y > 10:
            self.y = 10 - ( new_y - 10 )
        else:
            self.y = new_y


        self.life -= 1

        print(self.x,self.y,self.life)
        return (self.x,self.y)

    
    def eat(self):
        self.life += 20
        if self.life > 100:
            self.life = 100


class Fish():
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        new_x = self.x + r.choice([-1,1])
        new_y = self.y + r.choice([-1,1])

        if new_x < 0:
            self.x = 0 - ( new_x - 0 )
        elif new_x > 10:
            self.x = 10 - ( new_x - 10 )
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - ( new_y - 0 )
        elif new_y > 10:
            self.y = 10 - ( new_y - 10 )
        else:
            self.y = new_y

        return(self.x,self.y)


turtle = Turtle()
fish = []

for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if len(fish) == 0:
        print("鱼被吃光了，游戏结束。")
        break
    if turtle.life == 0:
        print('小甲鱼饿死了，游戏结束。')
        break

    t = turtle.turtle_move()
    for each_fish in fish[:]:
        if each_fish.move() == t:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼被吃掉了。")

        

