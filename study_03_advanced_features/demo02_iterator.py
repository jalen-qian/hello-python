from collections.abc import Iterable

"""
迭代：
Python的迭代抽象程度更高，像Java、c语言通过 for i=0; i< n ; i++ {} 来迭代，本质上是通过下标来迭代的。
Python的迭代不仅限于 list tuple 等有下标的数据结构，还有 dict等没有下标的数据结构，无论有没有下标，都可以迭代。
Python可以迭代任何可迭代的对象。
"""

'''1.迭代list & tuple'''
list1 = ['hello', 1, 'hahaha']
for v in list1:
    print(v)

tuple1 = ('广州', '深圳', '上海')
for v in tuple1:
    print(v)

'''2.迭代字典'''

dict1 = {'name': '张三', 'age': 19, 'id_card': 'xxxx', 'gender': '女'}
# 迭代key
for key in dict1:
    print(key)

# 迭代value
for v in dict1.values():
    print(v)

# 迭代 k - v
for k, v in dict1.items():
    print(k, ':', v)

# 迭代字符串

str = "我爱你祖国！"

for s in str:
    print(s)

"""
怎么区分可迭代对象？
我们发现，通过 for 循环，只要数据是可迭代对象，就可以执行下去，我们并不用关心数据是什么类型。
那么怎么知道一个对象是否是可迭代对象呢？

通过 collections.abc 模块的 Iterable 类型来判断。
可迭代对象都是这个接口的子类。
"""

print("list是否可以迭代：", isinstance([1, 2, 3], Iterable))
print("tuple是否可以迭代：", isinstance((1, 2, 3), Iterable))
print("dict是否可以迭代：", isinstance({'name': 'jalen'}, Iterable))
print('字符串是否可以迭代', isinstance('hello', Iterable))
print('数字是否可以迭代', isinstance(123, Iterable))  # False

"""
如果需要像其他语言一样，对一个 list 既迭代索引又迭代值怎么办？
可以使用 enumerate 函数把一个 list 变成一个索引-元素对，然后通过for循环遍历
"""

list2 = ['中国', '美国', '日本']
# 0 中国
# 1 美国
# 2 日本
for i, v in enumerate(list2):
    print(i, v)

"""
for循环支持多个变量接收参数，所以Python支持对一个二维list通过多个变量来遍历：
"""

list3 = [('name', '张三'), ('age', 18), ('gender', '女')]
# name 张三
# age 18
# gender 女
for k, v in list3:
    print(k, v)

list4 = [[1, 2, 3, 4], [5, 6, 7, 8], (9, 10, 11, 12)]
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
for a, b, c, d in list4:
    print(a, b, c, d)

"""
小练习：
找最大、最小值，返回一个tuple，如果传入的list是空，返回(None, None)
"""


def find_min_and_max(L):
    if len(L) > 0:
        minOne, maxOne = L[0], L[0]
        for v in L:
            minOne = min(minOne, v)
            maxOne = max(maxOne, v)
        return minOne, maxOne
    else:
        return None, None


if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
