from functools import reduce

"""
Python内建了两个功能强大的高阶函数。map()和reduce()
"""

"""
1.map(f,iterable)函数接收两个参数，第一个是一个函数，第二个是Iterable
map()函数将f作用在iterable的每个元素上，并返回一个Iterator
"""
'''示例1）得到一个list的平方序列'''
# 这个用列表生成式可以做，如下：
print([n * n for n in range(1, 6)])  # [1, 4, 9, 16, 25][1, 4, 9, 16, 25]


# 也可以用map()函数
def f(x):
    return x * x


# 由于map返回的是一个Iterator，Iterator是惰性的，所以需要通过list()函数
# 把Iterator的所有结果计算出来，并生成一个list
print(list(map(f, [1, 2, 3, 4, 5])))  # [1, 4, 9, 16, 25]

'''示例2）把一个list的所有数字转换成字符串'''
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

"""
2.reduce()函数
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

使用reduce 必须引入 :
from functools import reduce
"""

'''示例1）利用reduce()求list的和'''


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))  # 15

'''
示例2）利用reduce将list转数字
当然系统内置了sum()函数可以做这件事，但是如果要将list转成数字，sum就做不到了
[1,3,4,5,6] => 13456
'''
print(sum([1, 2, 3, 4, 5]))


def fn(x, y):
    return x * 10 + y


# 13456
print(reduce(fn, [1, 3, 4, 5, 6]))

'''
示例3）字符串转数字
由于str也是一个序列，所以综合上面的两个示例 ，可以将str用map()先转换为一个数字list，然后用reduce转换为数字
'''


def char2num(c):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[c]


print(reduce(fn, map(char2num, '12345')))

'''整理成一个函数，就是：'''
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2num(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2num('123'))

'''用lambda表达式进一步简化就是：'''


def str2num2(s):
    def char2num(s):
        return DIGITS[s]

    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2num2('456'))

"""
练习1：
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
"""


# def normalize(name):
#     return name.capitalize()

def normalize(name):
    return name[0].upper() + name[1:].lower()


print(list(map(normalize, ['adam', 'LISA', 'barT'])))
