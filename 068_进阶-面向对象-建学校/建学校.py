# 创建北京和成都两个校区
'''
1.创建 Linux\Python 两个课程
2.创建北京校区的Python3期课程和成都校区的Linux 1期课程
3.管理员创建了北京区的学员小张，并将其分配给了Python3期
4.管理员创建了讲师小周，并将其分配给了Python3期
5.讲师小周创建了一条Python3期的上课记录Day02
6.讲师小周为Day02这节课所有的学院批改了作业，小张得了A，小王得了B
7.学员小李查看了自己所报的课程
8.学员小李在查看了自己在python3的成绩列表然后退出了
9.学员小张给了讲师小周好评。
'''
class School():
    def __init__(self,school_name):
        self.school_name = school_name
        self.teachers_list = []
        self.students_list = []
# 学校需要做些什么呢？  1.找老师，2.招生，3.提供课程，4.。。。

    def hire_teachers(self,teacher_name,age,sex,school_location,subject):
        # 发现需要一个list存储teachers，所以在构造函数中先创建一个空list
        self.teachers_list.append(teacher_name)
        print("{}校区聘请了{}担任{}的教学工作。".format(school_location,teacher_name,subject))

    def enroll_students(self,student_name,age,sex,school_location,subject):
        self.students_list.append(student_name)
        print("{}校区又招到了一位新学员{}，将会加入{}课程的学习".format(school_location,student_name,subject))


class Subject(School):
    def __init__(self,school_name,subject_name,term):
        super(Subject,self).__init__(school_name)
        self.subject_name = subject_name
        self.term = term

        print("我们现在有{}校区{}{}课程".format(self.school_name,self.subject_name,self.term))     # 调用就打印信息


    def subject_info(self):
        print("学校的{}课程安排是：D1,D2,D3,D4,.....".format(self.subject_name))



Python = Subject("BJ", "Python",3)
Linux = Subject("CD", "Linux",1)


        
class Teachers():
