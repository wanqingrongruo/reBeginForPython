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
