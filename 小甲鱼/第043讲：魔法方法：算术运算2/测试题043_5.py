class C():
    count = 0 #静态属性
    def __init__(self):
        C.count += 1

    @staticmethod # 该修饰符表示 static（）是静态方法
    
    def static(arg1,arg2,arg3):
        print(arg1,arg2,arg3,arg1+arg2+arg3)

    def nosatic(self):
        print("I'm the normal method!")


