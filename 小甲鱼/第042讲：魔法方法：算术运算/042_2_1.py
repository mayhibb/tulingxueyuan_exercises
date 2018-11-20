class Nstr(str):
    def __init__(self,string):
        self.n = 0
        self.string = str(string)
        for i in self.string:
            self.n = self.n + ord(i)


    def __add__(self,other):
        return self.n + other.n

