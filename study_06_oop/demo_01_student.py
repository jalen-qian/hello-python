#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s:%d" % (self.__name, self.__score))

    def get_grade(self):
        if self.__score > 90:
            return 'A'
        elif self.__score > 60:
            return 'B'
        else:
            return 'C'


jalen = Student('Jalen', 80)
aimi = Student('Aimi', 98)

jalen.print_score()
print(jalen.get_grade())
aimi.print_score()
print(aimi.get_grade())

"""可以自由绑定属性"""
jalen.age = 45
print(jalen.age)

"""__开头的是私有属性，不可以访问"""
# AttributeError: 'student' object has no attribute '__name'
# print(jalen.__name)

"""如果强行访问，事实上python将 __name 解析成了 _Student__name """
"""但是不建议这样访问，而且不同的Python解释器解释成的变量名不一定相同。"""
print(jalen._Student__name)  # Jalen

"""由于__name被解析为了_Student__name，所以下面的方法设置__name不会成功，会增加一个新的属性__name"""
jalen.__name = '张三'
jalen.print_score()  # Jalen:80 打印出来仍然是Jalen
print(jalen.__name)  # 张三
