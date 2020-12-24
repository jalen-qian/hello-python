"""
高级特性1：切片
和Go语言类似，Python支持对list、tuple、字符串进行切片操作
"""

'''
1.取一个list或者tuple前3个
'''
names = ['Jalen', 'Mike', 'Susan', 'Michale']
# ['Jalen', 'Mike', 'Susan']
print(names[0:3])

t = (0, 1, 2, 3, 4)
# (0, 1, 2)
print(t[0:3])

# 如果从0开始，可以省略
print(t[:3])

'''
2.倒着取
'''
# ['Mike', 'Susan'] 注意 -1位置的不包含，因为是切片操作的区间是左闭右开
print(names[-3:-1])

# 要包含最后一个位置，可以省略-1
# ['Mike', 'Susan', 'Michale']
print(names[-3:])

'''
构造一个包含100个数的list [1,100]
'''
nums = [num + 1 for num in range(100)]

'''取前10个数'''
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[:10])

'''取后10个数'''
# [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print(nums[-10:])

'''前 11 - 20个数'''
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(nums[10:20])

'''前10个数，每2个取1个，得到奇数序列'''
# [1, 3, 5, 7, 9]
print(nums[:10:2])

'''前10个数，每2个取1个，得到偶数序列'''
# [2, 4, 6, 8, 10]
print(nums[1:11:2])

'''所有的数，每5个取一个'''
# [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]
print(nums[::5])

'''什么都不写，用[:]可以copy一个list'''
names2 = names[:]
# ['Jalen', 'Mike', 'Susan', 'Michale']
print(names2)
names2[0] = 'Jack'
print(names)  # ['Jalen', 'Mike', 'Susan', 'Michale']
print(names2)  # ['Jack', 'Mike', 'Susan', 'Michale']

names3 = names2
names3[0] = 'Tom'
# 不拷贝的时候，改变names3,names2也会变
print(names2)  # ['Tom', 'Mike', 'Susan', 'Michale']

"""
字符串切片：
"""
str1 = "我爱中国"

# 我爱
print(str1[:2])

str2 = 'I am 中国人'

# am 中
print(str2[2:6])

"""
小练习：
利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
"""


def trim(s):
    start_idx, end_idx = 0, len(s)
    for c in s:
        if c == ' ':
            start_idx = start_idx + 1
        else:
            break

    for c in reversed(s):
        if c == ' ':
            end_idx = end_idx - 1
        else:
            break

    return s[start_idx:end_idx]


print(trim('  hello  '))
print(trim('ssss    '))
print(trim(' ssss   ss    '))