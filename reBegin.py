import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs heart'.split()

    def __init__(self):
        self._cards =  [Card(rank, suit) for suit in self.suits
                                         for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

# 列表推导使用原则: 只用列表推导来创建新的列表,并且尽量保持简短
codes = [i*i for i in range(1, 10)]
print(codes)
symbols = '@#$%$$'
beyond_ascii =  [ord(s) for s in symbols if ord(s) > 35]
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
b,a = a,b
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
metro_areas = [('Tokyo', 'JP', (35.689733, 139.691667)), ('Tokyo1', 'JP', (35.689733, 139.691667)), ('Tokyo2', 'JP', (35.689733, 139.691667)), ('Tokyo3', 'JP', (35.689733, 139.691667))]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.6f} | {:9.6f}' # 格式化
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