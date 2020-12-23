"""
函数参数：
共有5种：
必选参数、默认参数、可变参数、关键字参数和命名关键字参数

小结
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

"""


# 计算平方
# def power(x):
#     return x * x
#
#
# print(power(2))
# 如果需要计算 x ^ n 呢？写n个函数？

# 通过默认参数，可以解决此问题，默认为2，计算平方
def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


print(power(5))


def add_end(L=[]):
    """默认参数的默认值，必须指向“不可变对象”！！！"""
    L.append('end')
    return L


# ['end']
print(add_end())
# ['end', 'end']
# 为什么第二次调用会出现两个'end' ?
# 因为函数add_end()的参数L在第一次执行时，指向了可变的对象[]，第二次调用append是对同一个对象调用 L.append()
print(add_end())


# 优化：将默认参数赋值为不可变的 None
def add_end2(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


# 现在打印的都是 ['end']
print(add_end2())
print(add_end2())


# 默认参数的传参如果不按照定义的顺序，需要指定参数名称
def enroll(name, gender, city='北京', age=16):
    print('name', name)
    print('gender', gender)
    print('city', city)
    print('age', age)


enroll('小明', '男')

# 跳过了city，直接传age，需要显示指定参数名，city仍然会取默认值 '北京'
enroll('小红', '女', age=22)

"""
可变参数：
函数参数个数不确定，可以是0个或者多个
举例：给定一组数 a,b,c,d... 计算并返回 a^2 + b^2 + c^2 +...
"""


# 方法一：参数指定为一个list或者tuple
def calc(nums):
    sum = 0
    for n in nums:
        sum += n * n
    return sum


print(calc([1, 2, 3, 4]))
print(calc((4, 5, 3, 2)))


# 为了简化调用函数的参数为 calc(1, 2, 3, 4) 可以使用 *来定义可变参数
# 可变参数在函数中接收到的是一个 tuple
def calc(*nums):
    sum = 0
    for n in nums:
        sum += n * n
    return sum


print(calc(1, 2, 3))  # 14

# 如果已经有两个 list 或者 tuple类型的变量了，如何传入呢
# 答案是加一个*
a = [1, 2, 3, 4, 5]
print(calc(*a))

"""
关键字参数
如果传入的数据是结构化的，又需要参数个数不固定，怎么办？
可以定义关键字参数，关键字参数会将传入的参数变成一个 dict （字典）
"""


def person(name, age, **other):
    print("name:", name, "age:", age, "other:", other)


person("张三", 26, height=155)  # name: 张三 age: 26 other: {'height': 155}

person("李四", 28, city='北京', gender='男')  # name: 李四 age: 28 other: {'city': '北京', 'gender': '男'}

# 如果已经有了一个dict，只需要前面加**
params = {
    "id_card": '54555445',
    "gender": '女'
}
# 你可以这样写
person('王五', 32, idcard=params['id_card'], gender=params['gender'])
# 但是没必要，可以直接**
person('王五', 32, **params)

"""
命名关键字参数：
关键字参数解决了需要传入参数个数不固定，且参数是键值对的应用场景，这些键值对可以是任意的，没有限制
比如我们如果规定必须传入 id_card 和 gender ，那么就必须在person()函数里面做参数校验
"""


def person(name, age, **other):
    if (not 'id_card' in other) or (not 'gender' in other):
        print('others 必须包含\'id_card\' 和 \'gender\'')
        return
    print("name:", name, "age:", age, "other:", other)


# name: 张三 age: 18 other: {'city': '上海', 'id_card': '232323', 'gender': '女'}
person('张三', 18, city='上海', id_card='232323', gender='女')

# others 必须包含'id_card' 和 'gender'
person('张三', 18, city='上海', gender='女')

"""
命名关键字参数用法：
我们可以定义“命名关键字参数”来规定传入的键值对必须有哪些key
*后面的参数，就是命名关键字参数，规定了
"""


# 命名关键字参数需要在 *的后面
def person(name, age, *, id_card, gender):
    print('name:', name, 'age:', age, 'id_card:', id_card, 'gender:', gender)


# 传参时传入的必须是键值对，函数内获取的是值
# name: 张三 age: 18 id_card: 333333 gender: 33
person('张三', 18, id_card='333333', gender=33)


# 如果已经有了一个可变参数，可变参数后面的参数就是命名关键字参数，不需要额外的*
def person(name, age, *args, id_card, gender):
    print('name:', name, 'age:', age, 'args:', args, 'id_card:', id_card, 'gender:', gender)


# name: 张三 age: 26 args: ('hello', 'world') id_card: 2458841 gender: 女
person('张三', 26, 'hello', 'world', id_card='2458841', gender='女')

"""
五种参数混合使用：
Python函数的5种参数可以混合定义，但是必须按照
必选参数、默认参数、可变参数、命名关键字参数 和 关键字参数的顺序
"""

"""
定义
"""


def f1(a, b, c=2, *d, e, f, **g):
    print(a, b, c, d, e, f, g)


f1('a是必选参数', 'b是必选参数', 3, 'hello', 'world', e='e是命名关键字参数', g1='关键字参数', g2='关键字参数2')

"""
命名关键字参数 和 关键字参数的异同
相同点：两者在传参时都是传入键值对 a = xxx的形式
不同点：
        1.命名关键字参数传入的个数有限，定义了多少个就必须传多少个，且参数key的名字要对应
          关键字参数传入参数个数没限制，传入多少个就接收多少个
          
        2.命名关键字参数接收到的是参数值本身
          关键字参数接收到的是一个dict
          
        3.命名关键字参数定义了必须传，不传会报错
          关键字参数可以不传，不传的话接收到的是一个空的dict

其实可以这样理解：命名关键字参数也是一种必选参数（普通参数），只不过在可变参数之后，如果传参时不指定key名称，就不知道传入的
参数应该归属到可变参数的一部分，还是命名关键字参数，所以指定命名关键字参数在传参时才必须传入键值对
"""
