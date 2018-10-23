# 定义一个列表的操作类   ListInfo
'''
1.列表元素添加 add_key()
2.列表元素取值  get_key()
3.列表合并： update_list(list)
4.删除并且返回最后一个元素 del_key()
'''

class ListInfo():
    def __init__(self,list0):
        self.list0 = list0

    def add_key(self,key):
        self.list0.append(key)
        print(self.list0)

    def get_key(self,key):
        if isinstance(key,int) :
            if key >= 0 and key < len(self.list0): # 判断索引值
                return self.list0[int(key)]
            else:
                print( "索引超出了范围，请输入0至{0}的整数".format(len(self.list0)-1))
        else:
            print("参数无效，请输入一个整数。")

    def get_list(self):
        return self.list0

    def update_list(self,list1):
        self.list0.extend(list1)
        return self.list0

    def del_key(self):
        if len(self.list0) == 0 :
            return "列表已清空。" # 判断是否可以操作。。。。。
        else:
            return self.list0.pop()


l = ListInfo(['a', 'b', 'c', 'd', 'e', 'f'])
