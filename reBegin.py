import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs heart'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# 列表推导使用原则: 只用列表推导来创建新的列表,并且尽量保持简短
codes = [i * i for i in range(1, 10)]
print(codes)
symbols = '@#$%$$'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 35]
print(beyond_ascii)
b_a_02 = list(filter(lambda c: c > 35, map(ord, symbols)))
print(b_a_02)
## 笛卡尔积
colors = ['black', 'white', 'red']
sizes = ['s', 'm', 'l', 'xl']
tshirts = [(c, s) for c in colors for s in sizes]
print(tshirts)

# 生成器表达式 => ()
tu = tuple(ord(s) for s in symbols)
print(tu)
import array

a = array.array('I', (ord(s) for s in symbols))
print(a)

# tuple
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE32567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
## 平行赋值
a = 3
b = 4
b, a = a, b
print('a=%s,b=%s' % (a, b))
tt = (20, 8)
## *运算符把一个可迭代的对象拆开作为一个函数的参数
print(divmod(*tt))

import os

_, lastFileName = os.path.split('/Users/roni/Desktop/python/rebegin')
print('lastFileName: %s' % lastFileName)
## * 表示剩下的元素
c, d, *rest = range(5)
print(c, d, rest)
## 嵌套元组拆包
metro_areas = [('Tokyo', 'JP', (35.689733, 139.691667)), ('Tokyo1', 'JP', (35.689733, 139.691667)),
               ('Tokyo2', 'JP', (35.689733, 139.691667)), ('Tokyo3', 'JP', (35.689733, 139.691667))]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.6f} | {:9.6f}'  # 格式化
for name, cc, (latitude, longitude) in metro_areas:
    if longitude >= 0:
        print(fmt.format(name, latitude, longitude))

## 具名元组
from collections import namedtuple

### 创建一个具名数组需要两个参数, 一个是类名,,另一个是类的各个字段,,
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(City._fields)
ccc = City._make(tokyo)
print(ccc)
for key, value in ccc._asdict().items():
    print(key + ':', value)

## 作为不可变列表的元组  -- 第57页

# 切片
## 切片和区间会忽略最后一个元素
## 对对象进行切片
s = 'bicycle'
print(s[::3])
print(s[::-1])
## 多维切片和省略
## 给切片赋值
l = list(range(10))
l[2:5] = [20, 30]
del l[5:7]
l[3::2] = [11, 22]
print(l)
# 对序列使用+和* => 产生新序列, 不修改原有的序列
print(l + l)
print(l * 3)
## 建立由列表组成的列表 => 二维???
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board[1][2])
print(board)

# 序列的增量赋值 += => __iadd__     *= => __imul__
ll = [1, 2, 3]
ill = id(ll)
print(ill)
ll *= 2  # 可变序列不创建新变量
print(ll)
print(id(ll))

tt = (1, 2, 3)
itt = id(tt)
print(itt)
tt *= 2  # 不可变序列创建新变量
print(tt)
print(id(tt))

## 不要把可变对象放在元组
## 增量赋值不是一个原子操作
# it = (1, 2, [30, 40])
# it[2] += [50, 60]
# print(it)

# list.sort 方法和内置函数 sorted
print(l.sort())  # 返回值是 none
print(sorted(l))  # 有返回值,可以接受任何形式的可迭代对象做参数

# 用 bisect 来管理已排序的序列  bisect模块包含 bisect和 insort 两个主要函数,都是利用二分查找算法在有序序列中查找或插入元素
## 用 bisect 来搜索

# import bisect
# import sys
#
# HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
# NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# Row_Fmt = '{0:2d} @ {1:2d}  {2}{0:<2d}'
# def demo(bisect_fn):
#     for needle in reversed(NEEDLES):
#         position = bisect_fn(HAYSTACK, needle)
#         offset = position * ' |'
#         print(Row_Fmt.format(needle, position, offset))
# if __name__ == '__main__':
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect
#     print('DEMO:', bisect_fn.__name__)
#     print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
#     demo(bisect_fn)

## bisect.insort
# import  bisect
# import  random
#
# SIZE = 7
# random.seed(1729)
# my_list = []
# for i in range(SIZE):
#     new_item = random.randrange(SIZE*2)
#     bisect.insort(my_list, new_item)
#     print('%2d ->' % new_item, my_list)

# 数组
from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))  # 'd' 是类型码
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 7)
fp.close()
print(floats2[-1])
print(floats == floats2)

## memoryView 内存视图
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
