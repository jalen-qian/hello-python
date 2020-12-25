"""
生成器 Generator:
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

"""

'''示例1：生成i位置的平方的生成器'''

g = (i * i for i in range(1, 5))
# <generator object <genexpr> at 0x000001F11C0BDCC8>
print(g)

"""
生成器是把某种算法封装了起来，通过不断调用 next(g) 或者 g.__next__() 就可以不断计算出下一个结果
"""
# 1
# 4
# 9
# 16
print(g.__next__())
print(g.__next__())
print(next(g))
print(next(g))
# 没有更多的元素时，抛出StopIteration的错误。
# Traceback (most recent call last):
# print(next(g))


"""
生成器一直调用next(g)是比较笨的办法，而且会导致抛出 StopIteration 错误
由于生成器也是一个可迭代对象，所以可以用for循环，而且不会越界
"""
g2 = (i * i * i for i in range(1, 5))
# 1
# 8
# 27
# 64
for n in g2:
    print(n)

"""
如果算法比较复杂，还可以用函数生成生成器（yield关键字用法）
具有推导性质的算法，都可以通过函数写出生成器，比如斐波那契数列。
"""

"""首先斐波那契数列是一个递归的算法"""


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 任何递归都能写成循环的形式
print("====fib2====")


def fib2(max):
    a, b, n = 0, 1, 0
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    print('done')


# 1 1 2 3 5 8 13 21
fib2(8)
"""
可以发现，这里的fib2()定义了斐波那契数列的推导规则，可以从第1个数开始，推导出后续的任意一个数。
这个性质和生成器如出一辙。在这个例子中，只要把打印b的语句，改成 yield b , 这个fib2()函数就是
一个生成器。
"""


def fib3(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 打印fib3(5)发现是一个generator
# <generator object fib3 at 0x00000258A87EDD48>
print(fib3(5))

"""
虽然这里是函数的形式，但是生成器和普通的函数很不同，普通函数是顺序执行到最后一行，或者遇到了return，就返回结果。
而生成器是不断调用next()，每调用一次next()时，程序执行到 yield 语句就返回，此时程序停到这个语句这里，再次执行
next()时，从上一次的 yield 语句的地方继续执行。
"""
# 1
# 1
# 2
# 3
# 5
for num in fib3(5):
    print(num)

"""举个栗子："""

print('====odd====')


def odd():
    print('step1:')
    yield 1
    print('step2:')
    yield 3
    print('step3:')
    yield 5


o = odd()
# step1:
# 1
print(next(o))
# step2:
# 3
print(next(o))
# step3:
# 5
print(next(o))

"""
上面打印fib数列时，我们发现 return 语句返回的 'done' 没有打印出来，这是因为for循环只会拿 yield 中的值
事实上如果 执行到 return ，说明已经越界了，程序会抛出 StopIteration 错误，并将 return 的值放到 StopIteration
错误的value值中，我们可以通过捕获这个异常拿到。
"""

f = fib3(6)
# 1
# 1
# 2
# 3
# 5
# 8
# done
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print(e.value)
        # 拿到return的值立马break
        break

"""
练习
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
"""


def triangles():
    pass
    # la, lb, a, b = 0, 0, 1, 0
    # while True:
    #     cur = [1]
    #     while lb > 0:
    #         cur.append()


"""
小结：
generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。

要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

请注意区分普通函数和generator函数，普通函数调用直接返回结果，generator函数调用返回的是一个generator对象
"""
