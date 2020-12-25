#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 这是一个测试模块，用来测试sys.argv'

__author__ = 'Jalen Qian'

import sys


def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello, %s' % args[1])
    else:
        print('too many arguments!')


"""
作用域：
正常命名的变量是public的，可以被外部引用
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量
_xxx这样的变量属于private的，不可以被外部引用。
"""


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


"""
当我们用Python3 hello.py运行时，Python解释器把一个特殊变量 __name__ 置为 __main__ ，
而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
最常见的就是运行测试。
"""
if __name__ == '__main__':
    test()
    print(greeting('hello'))
