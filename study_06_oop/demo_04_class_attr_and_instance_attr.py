"""
类属性和实例属性
类属性：属于某个类，相当于Java的静态属性，直接定义在类里面
实例属性：属于某个实例，通过实例变量，或者 self关键字来指定和访问
"""


class Student(object):
    name = 'student'  # 类属性

    def __init__(self, name, score):
        self.name = name  # 实例属性
        self.score = score


s1 = Student('Bob', 89)

# 通过实例变量访问实例属性
print(s1.name, s1.score)  # Bob 89
# 实例属性比类属性有更高的优先级，所以实例属性被赋值
s1.name = "Jack"
# Jack student
print(s1.name, Student.name)

# 通过类变量来访问类属性
print(Student.name)  # student

'''可以通过del删除实例属性 或者 类属性'''
del s1.name
# 实例属性被删除后，访问到的是类属性
# s1.name: student
print('s1.name:', s1.name)

'''删除类属性'''
del Student.name

# 删除后，由于实例属性和类属性都没有了，所以访问会报错：
# AttributeError: 'Student' object has no attribute 'name'
# print('s1.name:', s1.name)


"""
为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
"""


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')