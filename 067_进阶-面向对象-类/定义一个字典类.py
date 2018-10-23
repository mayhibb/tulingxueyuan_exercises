# 定义一个字典类：DictClass ,完成如下功能
"""
1、删除某个key  del_dict(key)
2、判断某个键是否在字典里，如果在，返回键对应的值，反之，返回“not found” get_dict()
3、返回键组成的列表,返回类型list  get_key()
4、合并字典，并且返回合并后字典的values组成的列表，返回类型list update_dict()

"""

class DictClass():

    def __init__(self,dict0):
        self.dict0 = dict0

    def del_dict(self,key):
        if key not in self.dict0.keys():
            print("not found")
        else:
            self.dict0.pop(key)
            print("删除成功！")

    def get_dict(self,key):
        if key in self.dict0.keys():
            return self.dict0[key]
        else:
            print('not found')

    def get_key(self):
        return slef.dict0.keys()

    def update_dict(self,dict1):
    # 练习中，（self,**dict1）,可以用多个字典更新
        self.dict0.update(dict1)
        return self.dict0.values()

d = DictClass({'a':1 , 'b':2 , 'c':3})
