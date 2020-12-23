"""
函数递归
"""


# 求一个数n的阶乘
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(100))

"""
练习：汉诺塔
汉诺塔的移动可以用递归函数非常简单地实现。

请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
move(3, 'A', 'B', 'c')
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
"""

