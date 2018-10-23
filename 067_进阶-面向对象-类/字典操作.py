class DictClass():
    def __init__(self,dict0={"a":1, "b":2}):
        self.dict0 = dict0

    def del_dict(self,key):
        if key not in self.dict0.keys():
            return 'key不在字典中'
        else:
            self.dict0.pop(key)
            print("删除成功")

    def get_key(self,key):
        if key not in self.dict0.keys():
            return 'not found'
        else:
            return self.dict0[key]

    def get_keys(self):
        return self.dict0.keys()

    def update_dict(self,dict1):
        self.dict0.update(dict1)
        return self.dict0.values()
        
d = DictClass()
