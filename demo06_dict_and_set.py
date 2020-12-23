"""
字典和集合
"""

'''
字典相当于其他语言中的map 是 key-value键值对 查找时间复杂度是O(1)
'''
d = {
    "Jack": 60,
    "Jalen": 99,
    "Tom": 78,
}
print(d["Jack"])  # 60

# 字典中的key不可重复，如果重复赋值，会覆盖掉
d["Jack"] = 80  # 覆盖
d["Alice"] = 100  # 重新添加一个key
print(d["Jack"], d["Alice"])  # 80 100

# print(d["Jason"])  # 访问不存在的key，会报错 KeyError: 'Jason'

# 通过 in 关键字判断一个key是否存在
if "Jason" in d:
    print("Jason exists")
else:
    print("Jason not exists")

# 通过dic.get()方法，如果key不存在，会返回none，或者自定义的值
score = d.get("Jason")
print(score)  # None

score = d.get("Jason", -1)
print(score)  # -1

# 删除key
score = d.pop("Alice")
print(score, d)  # 100 {'Jack': 80, 'Jalen': 99, 'Tom': 78}

'''
set 集合，和list一样是用来存储一组元素的，不是key-value键值对
不同点：set 是无序；set 中的元素不能重复
'''
s1 = {1, 2, 3}
print(s1)  # {1, 2, 3}

# 通过一个list创建set，会自动过滤重复元素
s2 = set([1, 2, 2, 2, 3, 3, 4])
print(s2)  # {1, 2, 3, 4}

# add 添加
s2.add('hello')

print(s2)  # {'hello', 1, 2, 3, 4}

# 重复添加不会有效果
s2.add('hello')
print(s2)  # {'hello', 1, 2, 3, 4}

# set 删除 remove
s2.remove('hello')
print(s2)

'''
由于set和数学上的“集合”概念一致，所以可以求交集、并集、差集
'''
s1 = {1, 2, 3}
s2 = {2, 3, 4, 5}
print("交集", s1 & s2)  # 交集 {2, 3}
print("并集", s1 | s2)  # 并集 {1, 2, 3, 4, 5}
print("差集", s2 - s1)  # 差集 {4, 5}
