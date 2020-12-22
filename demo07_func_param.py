"""
函数参数
"""


# 计算平方
# def power(x):
#     return x * x
#
#
# print(power(2))


def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


print(power(5))

"""
可变参数的默认值，必须指向“不可变对象”！！！
"""


def add_end(L=[]):
    L.append('end')
    return L


# ['end']
print(add_end())
# ['end', 'end']
# 为什么第二次调用会出现两个'end' ?
# 因为函数add_end()的参数L在第一次执行时，指向了可变的对象[]，第二次调用append是对同一个对象调用
print(add_end())


# 优化：将默认参数赋值为不可变的 None
def add_end2(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


# 现在打印的都是 ['end']
print(add_end2())
print(add_end2())
