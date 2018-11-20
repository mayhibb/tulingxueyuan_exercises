import time as t

class Timer():
    def __init__(self):
        self.prompt = "未开始计时！"
        self.start_time = 0
        self.stop_time = 0
        self.name_list = ["年","月","天","小时","分钟","秒"]

    def __str__(self):
        return self.prompt
    __repr__ = __str__

    def __add__(self,other):
        prompt = "总共用时为："
        result = []
        for i in range(6):
            result.append(self.calc_list[i] + other.calc_list[i])
            if result[i]:
                prompt += (str(result[i]) + str(self.name_list[i]))
        print(prompt)

    #开始计时

    def start(self):
        self.prompt = "提示：请调用stop()停止计时"
        print("计时开始……")
        self.start_time = t.localtime()
        

    # 结束计时
    def stop(self):
        if self.start_time == 0 :
            print("请先调用start()开始计时")
            
        else:
            self.stop_time = t.localtime()
            self._calculate()
            print("计时结束……")

        
    # 计算时间差
    def _calculate(self):
        self.prompt = "总共用时为："
        self.calc_list = []

        for i in range(6):
            self.calc_list.append(self.stop_time[i] - self.start_time[i])

            if self.calc_list[i] != 0:
                self.prompt += (str(self.calc_list[i])+str(self.name_list[i]))
        print(self.prompt)


        self.start_time = 0
        self.stop_time = 0
        
            

        

             

            
        
        
