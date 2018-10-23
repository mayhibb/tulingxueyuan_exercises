# 定义一个集合的操作类
'''
1.集合元素添加： add_key()
2.集合的交集： get_intersection()
3.集合的并集： get_union()
4.集合的差集：get_difference()
5.删除集合元素，返回删除成功，or 集合中没哟有指定元素。
'''

class SetInfo():
    def __init__(self,set0 = {}):
        self.set0 = set0

    def add_key(self,key):
        self.set0.add(key)
        return "添加成功。"

    def get_intersection(self,set1):
        if isinstance(set1,set) :  # 判断传入的类型
            return self.set0.intersection(set1)
        else:
            return "传入的不是set"

    def get_union(self,set2):
        if isinstance(set1,set) :
            return self.set0.union(set2)
        else:
            return "传入的不是set"

    def get_difference(self,set3):
        if isinstance(set1,set) :
            return self.set0.difference(set3)
        else:
            return "传入的不是set"

    def del_key(self,key):
        if key in self.set0 :
            self.set0.discard(key)
            print("删除成功。")
        else:
            return "集合中没有指定的元素。"


if __name__ == "__main__":
    s = SetInfo({0,1,2,3,4,5,6,7,8})
else:
    return None
