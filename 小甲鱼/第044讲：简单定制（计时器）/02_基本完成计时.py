import time as t

class Timer():

    #开始计时

    def start(self):
        print("计时开始……")
        self.start_time = t.localtime()
        self.time_list0 =[]

        for i in range(6):
            self.time_list0.append(self.start_time[i])

    # 结束计时
    def stop(self):
        self.stop_time = t.localtime()

        self.time_list1 = []
        
        for i in range(6):
            self.time_list1.append(self.stop_time[i])

        print("计时结束……")

        self.calculate()

    # 计算时间差
    def calculate(self):
        print("总共用时为：", end = "")
        self.clac_list = []

        for i in range(6):
            self.clac_list.append(self.time_list1[i] - self.time_list0[i])
            
            self.name = ["年","月","日","小时","分钟","秒"]
            print(self.clac_list[i],self.name[i] ,end ="  ")

            
        
        
