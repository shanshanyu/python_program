class Student(object):      
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        print("%s 正在学习" % self.name)


s = Student("tom",15)
s.study()
