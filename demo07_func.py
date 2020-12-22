"""
Python中的函数
内置函数可以访问 https://docs.python.org/3/library/functions.html查看
"""

import math

# 1.abs求绝对值
print(abs(10))
print(abs(-20))

# 2.hex返回一个整数小写的16进制表示法的字符串(0x开头)
print(hex(10))  # 0xa

'''
数据类型转换函数
'''
a = '12'
print(int(a))  # 12
b = 36.8
print(int(b))  # 36
c = '-20'
print(float(c))  # -20.0
d = ''
print(bool(d))  # False

"""
定义函数 def
"""


# 计算绝对值
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-20))  # 20

# 如果传入的值不是 int float类型，会报错
'''
TypeError: '>' not supported between instances of 'str' and 'int'
这里是因为 if x > 0报错，报错不友好，我们应该直接提示用户输入的类型是什么
'''
# print(my_abs('hello'))

'''
TypeError: bad operand type for abs(): 'str'
系统的提示比较友好
'''
# print(abs('hello'))

'''重新定义函数'''


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type for my_abs()")
    if x > 0:
        return x
    else:
        return -x


# print(my_abs('hello'))


# 返回多个值
# 给定一个坐标x y,位移值step和角度angle
# 计算出新的坐标
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x1, y1 = 10, 10
#  函数返回多个值，实际上是返回一个tuple!
print(move(x1, y1, 10, 30))  # (11.54251449887584, 19.880316240928618)
nx1, ny1 = move(0, 0, 10, 30)
print(nx1, ny1)

"""
练习
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解。
提示：
一元二次方程的求根公式为：
x = (-b +- sqrt(b^2 - 4ac)) / 2a 
计算平方根可以调用math.sqrt()函数：
"""


def quadratic(a, b, c):
    sq = math.sqrt(b * b - (4 * a * c))
    x1 = (-b + sq) / (2 * a)
    x2 = -(b + sq) / (2 * a)
    return x1, x2


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
