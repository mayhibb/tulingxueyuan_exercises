class Rectangle():
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height

    def __setattr__(self,name,value):
        if name == "square":
            self.width = value
            self.height = value

        #(无限递归)
        #else:
            #self.name = value

        # 第一种
        else:
            super().__setattr__(name,value)

        # 第二种方法
        #else:
            #self.__dict__[name] = value
        
       #self.getArea()
       #self._square()

    def getArea(self):
        return self.width * self.height

    def _square(self):
        if self.width == self.height:
            print("这是一个正方形，边长为:{0}。".format(self.width))
        else:
            print("这是一个矩形，长是：{0}；宽是：{1}。".format(self.width,self.height))
        
        
    
