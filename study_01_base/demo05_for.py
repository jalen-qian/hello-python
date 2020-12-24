"""
循环语句
"""

# 1.打印list中的值
names = ['Jalen', 'Jason', 'Bob', 'Michael']
for n in names:
    print(n)

# 2.从1 + 到10
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0
for n in nums:
    result += n

print(result)

# 3.如果要从1 + 到100呢？python提供了range()函数
# range(n)会返回从 0 到 n-1 的序列
nums = list(range(101))  # 0 1 2 3 ...100
result = 0
for n in nums:
    result += n
print(result)  # 5050

# 4.也可以直接遍历
result = 0
for n in range(101):
    result += n
print(result)  # 5050

# 5.while循环

n = 0
result = 0
while n < 100:
    n = n + 1
    result += n
print(result)

# 6.break
n = 0
result = 0
while True:
    if n >= 100:
        break
    n = n + 1
    result += n
print(result)

# 7.continue
# 打印 1 ~ 10中所有的偶数
for n in range(11):
    if n % 2 == 0:
        print(n)
