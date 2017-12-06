import sys
## 字典dictionary和集合 set

### hash table
tt = (1, 2, (30, 40))
print(hash(tt))
# tl = (1, 2, [30, 40])
# print(hash(tl))
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

### dict comprehension  字典推导
DIAL_CODES = [(86, 'China'), (91, 'India'),(1, 'United states'),(62, 'Indonesia'),(55, 'Brazil'),(7, 'Russia'),(81, 'Japan'),]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
code_country = {code: country.upper() for code, country in DIAL_CODES}
print(code_country)

### 常见的映射方法
import sys
import re

WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # occurences = index.get(word, [])
            # occurences.append(location)
            # index[word] = occurences
            index.setdefault(word, []).append(location) # setdefault 处理找不到的键
for word in sorted(index, key=str.upper):
    print(word, index[word])

### 映射的弹性键查询
#### defaultdict
from collections import defaultdict
dd = defaultdict(list)

class StrKeyDic(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return  self[str(key)]
    def __get__(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()

### 子类化 UserDict
from  collections import UserDict

class StrKeyDic00(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    def __contains__(self, item):
        return str(item) in self.data
    def __setitem__(self, key, value):
        self.data[str(key)] = value

