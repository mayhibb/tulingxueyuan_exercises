import time as t

class Timer():
    def __str__(self):
        return self.prompt

    __repr__ = __str__


    # 开始计时
    def start(self):
        self.start = t.localtime()
        print("计时开始...")

    # 计时结束
    def stop(self):
        self.stop = t.localtime()
        self._calc()
        print("计时结束！")

    # 内部方法，计算时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for i in range(6):
            self.lasted.append(self.stop[i] - self.start[i])
            self.prompt += str(self.lasted[i])
        
       
