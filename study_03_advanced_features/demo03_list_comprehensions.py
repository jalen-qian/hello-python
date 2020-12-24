import os

"""
列表生成式：
Python的列表生成式能够很方便的构造list
"""

"""实例一：生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"""

"""传统方法，要写for循环并赋值"""
l1 = []
for num in range(1, 11):
    l1.append(num)
print(l1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""列表生成式："""
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([num + 1 for num in range(10)])
# 或者
print([num for num in range(1, 11)])
# 或者
print(list(range(1, 11)))

"""示例二：生成[1*1, 2*2, 3*3, ... 10*10] """

"""传统办法："""
l2 = []
for i in range(1, 11):
    l2.append(i * i)
print(l2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""列表生成式："""
print([i * i for i in range(1, 11)])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""
示例3：
列表生成式中嵌入if条件判断

将偶数抽出来，也就是说，列表中的第i个数字是第i个偶数的平方，怎么写
[2*2, 4*4, 6*6, 8*8 10*10]
也是一行代码解决：
"""
print([i * i for i in range(1, 11) if i % 2 == 0])

"""
示例4：
列表生成式中多层for循环

比如：生成两个字符串的全排列：
'ABC' 'XYZ' => ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
"""
print([a + b for a in 'ABC' for b in 'XYZ'])

"""
示例5：实际应用
列出当前目录下所有文件和目录的名称
"""
print([file_name for file_name in os.listdir('.')])

"""
示例6：for循环使用多个参数
比如：将一个字典，以 key = value的形式生成一个list
使用dict.items()可以获取键值对
"""
dict1 = {
    "name": "张三",
    "age": '18',
    "gender": "男",
    "country": "中国"
}
# ['name = 张三', 'age = 18', 'gender = 男', 'country = 中国']
print([k + ' = ' + v for k, v in dict1.items()])

"""
示例7：
把一个list中所有的字符串都变成小写
1.调用str.lower()转小写
2.利用if 判断是字符串才处理，否则不是字符串的元素调用 lower()会报错
"""
list2 = ['Hello', "World", "IBM", "APPLE", 123]
# ['hello', 'world', 'ibm', 'apple']
print([s.lower() for s in list2 if isinstance(s, str)])

"""
示例8：if ... else
在列表生成式中，for 前面如果有if，那么必须带有else ,因为 for 前面的部分必须得到一个值，
如果只有if，那么如果不满足if的情况下，某次循环解析器都得不到值了，就会报错
如果for后面有if，则一定不能带有else, 因为这个if是过滤条件，是用来过滤某次for循环迭代到的值是否需要给到for前面的部分，所以一定不能有else
"""
# SyntaxError: invalid syntax
# print([n for n in range(1, 11) if n % 2 == 0 else 0])

# [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
print([n if n % 2 == 0 else -n for n in range(1, 11)])
