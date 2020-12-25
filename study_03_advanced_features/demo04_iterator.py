"""
迭代器：Iterator
像上一个demo中讲的Generator一样，能够通过 next(x) 函数调用不断拿到下一个，并在没有下一个值时，抛出 StopIteration
错误表示无法继续返回下一个值了。这样的对象都是迭代器对象。

我们知道，可以通过 for 循环来遍历的对象分为两种：
1）list 、tuple、dict、set、str
2）Generator
这些对象统称为 “可迭代对象 Iterable ”，判断方法是 isInstance(x,Iterable)
"""
from collections.abc import Iterable
from collections.abc import Iterator

# list [] 是否是Iterable: True
print('list [] 是否是Iterable:', isinstance([], Iterable))
# tuple (1,2) 是否是Iterable: True
print('tuple (1,2) 是否是Iterable:', isinstance((1, 2), Iterable))
# dict {"name":"张三"} 是否是Iterable: True
print('dict {"name":"张三"} 是否是Iterable:', isinstance({"name": "张三"}, Iterable))
# 字符串是否是Iterable: True
print('字符串是否是Iterable:', isinstance("sss", Iterable))
# Generator是否是Iterable: True
print('Generator是否是Iterable:', isinstance((i for i in range(10)), Iterable))

"""
能够通过 next(x) 函数调用不断拿到下一个的对象，属于“迭代器对象” Iterator
可以通过 isinstance(x, Iterator)来判断。
生成器都是 Iterator 对象，但是 list、dict、tuple、str 虽然是可迭代对象，但是不是迭代器对象
"""
print('Generator是否是Iterator:', isinstance((i for i in range(10)), Iterator))  # True
print('list 是否是Iterator:', isinstance([], Iterator))  # False

"""
虽然 list、dict、tuple、str 不是 iterator，但是可以通过 iter()函数将这些对象转换成 Iterator
"""
list1 = [i for i in range(1, 11)]
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iter_list1 = iter(list1)  # 通过iter()函数获取迭代器对象
print(next(iter_list1))  # 1
print(next(iter_list1))  # 2

"""
你可能会问，为什么list、dict、str等数据类型不是Iterator？

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，
只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
"""

"""
小结
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的，例如：
"""

for x in [1, 2, 3, 4, 5]:
    pass

"完全等价于："

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
