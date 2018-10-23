# 定义一个学生类，有下面的类属性
'''
1、姓名
2、年龄
3、成绩（语文，数学，英语）每科成绩类型为整数类方法
4、获取学生的姓名： get_name():返回类型为str
5、获取学生的年纪： get_age()：返回类型为 int
6、返回3门科目中最高的分数，get_score()返回类型 int
'''

class Student():
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_score(self):
        return max(self.scores)


s = Student("mayhibb", 18, [90,80,95])
