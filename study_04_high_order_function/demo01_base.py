"""
高阶函数：
"""
"""1.变量可以指向函数"""
# abs(-10)是函数调用
# 10
print(abs(-10))

# 函数名是函数本身
# <built-in function abs>
print(abs)

'''函数可以直接赋值给变量，函数名本身就是指向某个函数的变量'''
f = abs
# 10
print(f(-10))
# <built-in function abs>
print(f)

'''由于abs是指向一个求绝对值函数的变量，那么如果把这个变量重新赋值，能否重新调用呢？'''
# abs = 10
# TypeError: 'int' object is not callable
# print(abs(-10))

'''答案是不能，如果要使用abs，必须重启python环境'''
'''
注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，
要用import builtins; builtins.abs = 10。
'''

"""
2.函数可以作为参数传入
"""


def add(x, y, f):
    return f(x) + f(y)


# 15
print(add(-5, 10, abs))
