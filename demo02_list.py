# -*- coding: utf-8 -*-
# 有序的，可重复的集合
classmates = ['Jalen', 'jack', 'jason']
print(classmates)
print(classmates[0])
print(classmates[-1])  # 取最后一个位置的数据
print(classmates[-2])  # 取倒数第二个位置的数据

# 往位置1插入数据

classmates.insert(1, "Jack")
print(classmates)

classmates.insert(1, "Jack")
print(classmates)

# 删除最后一个位置的元素
last = classmates.pop()
print(last, classmates)

# 把某个元素替换成其他元素，直接赋值
classmates[1] = "Candy"
print(classmates)

# 嵌套list
list2 = ["广东", "湖南", "北京", ["广州", "深圳"], "上海"]
print(list2)

# list2的长度？
print(len(list2))  # 5
