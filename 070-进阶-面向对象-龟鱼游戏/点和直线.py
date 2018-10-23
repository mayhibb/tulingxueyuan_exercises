import math


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Line():
    def __init__(self, p1, p2):
        self.x = p1.get_x() - p2.get_x()
        self.y = p1.get_y() - p2.get_y()

        self.len = math.sqrt(self.x * self.x + self.y * self.y)

    def get_len(self):
        return self.len





def test():
    p1 = Point(2, 5)
    p2 = Point(5, 12)

    line = Line(p1, p2)
    print(line.get_len())
    
if __name__ == "__main__":
    test()
