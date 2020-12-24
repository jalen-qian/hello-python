"""
tuple和list不同，tuple不可以被改变，没有insert和pop函数，定义时就必须给定值，且确定了就不可改变
tuple因为不可改变，所以更安全。如果可以，尽量使用tuple代替list
"""
t1 = ("Jalen", "Jack", "Jason")
print(t1)  # ('Jalen', 'Jack', 'Jason')

# t1[0] = "Bob"  # 报错：TypeError: 'tuple' object does not support item assignment

print(t1)

# 空的tuple
t2 = ()
print(t2)  # ()

# 在定义只有一个元素，而且元素是数字类型时，会产生歧义
# 小括号可以既可以表示定义 tuple, 又可以表示数学公式，这时py解析器会认为这里是数学公式，把t3当作数字1
t3 = (1)
print(t3)  # 1

# 为了避免歧义，后面加一个逗号
t3 = (1,)
print(t3)  # (1,)
print(t3[0])

# "可变的" tuple ?
# 解释：durable的“不变”指的是指向的内存没有变，这里t4[2]指向的一直都是同一个list，list是可变的，这个list内部的值发生了替换
t4 = ('a', 'b', ['A', 'B'])
t4[2][0] = 'X'
t4[2][1] = 'Y'
print(t4)  # ('a', 'b', ['X', 'Y'])

# 请用索引取出下面的元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# Apple
print(L[0][0])
# Python
print(L[1][1])
# Lisa
print(L[2][2])
