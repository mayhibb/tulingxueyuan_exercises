class Count():
    def __init__(self,*args):
        if not args:
            print("没有参数传入！")

        else:
            print("传入了 {0} 个参数:".format(len(args)))
            for i in args:
                print(i,end="  ")
