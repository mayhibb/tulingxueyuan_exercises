class Student():
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        print(str(self.name))

    def get_age(self):
        print(int(self.age))

    def get_score(self,key):
        return self.scores[key]

    def get_max(self):
        scores_list = []
        scores_dict = {}
        for i in self.scores.keys():
            scores_list.append(self.scores[i])
            scores_dict[self.scores[i]] = i
        return scores_dict[max(scores_list)],max(scores_list)



# 同时返回，key和value，该怎么办（"Math":8）
# 上面这种吧value作为key，key变成value的方法会覆盖，原value相同的key值。




s = Student("yueyue",18,{"Math":8,"Chinese":80,"English":85,'physics':85})
