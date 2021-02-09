
import jsonpath

import re

str1 = "comeon,and go"
pattern = re.compile(r"comeon")
result1 = re.match(pattern, str1)  # match匹配以什么开头
print(result1.string)
print(result1.re)
print(result1.pos)
print(result1.lastindex)















