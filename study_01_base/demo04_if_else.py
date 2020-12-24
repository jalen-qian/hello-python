# -*- coding: utf-8 -*-
"""
条件判断

"""

age = 20

if age >= 18:
    print("your age is %d" % age)
    print("you are adult")

age = 3
if age >= 18:
    print("your age is %d" % age)
    print("you are adult")
else:
    print("your age is", age)
    print("you are a kid")

# elif 而不是 else if

'''
语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
所以这里打印teenager
'''
age = 16
if age < 10:
    print("child")
elif age <= 18:
    print("teenager")
else:
    print("adult")

# if x 简写
'''只要 x 是非零数字，非空list, 非空字符串，就为true '''
a = 10
if a:
    print("true")

# input
# 会报错，因为标准输入的数字是字符串类型，需要转换为int
# birth = input("birth:")
s = input("birth:")
birth = int(s)  # 如果输入的不是字符串，会报错
if birth < 2000:
    print("00前")
else:
    print("00后")

"""
小练习

小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
"""
height = 1.75
weight = 80.5
BMI = weight / (height * height)
print("小明的BMI:", BMI)
if BMI < 18.5:
    print("过轻")
elif BMI <= 25:
    print("正常")
elif BMI <= 28:
    print("过重")
elif BMI <= 32:
    print("肥胖")
else:
    print("严重肥胖")
