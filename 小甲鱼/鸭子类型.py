class Duck:
    def quack(self):
        print("呱呱呱")
    def feathers(self):
        print("这只鸭子有灰白灰白的羽毛")

class Person:
    def quack(self):
        print("你才是鸭子，你们全家都是鸭子")
    def feathers(self):
        print("这个人穿着一件鸭绒大衣")

def in_the_forest(duck):
    duck.quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)


game()
